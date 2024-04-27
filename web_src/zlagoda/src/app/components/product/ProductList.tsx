 import {
  Product,
  ProductArchetype,
  ProductCriteria,
  ProductListResponse, UserRole
 } from "../../../../generated";
import React, {useContext, useEffect, useState} from "react";
import {Checkbox} from "@mui/material";
import {GridColDef} from '@mui/x-data-grid';
import ListComponent, {getDefaultBaseCriteria} from "@/app/components/common/ListComponent";
 import {AlertContext} from "@/app/services/AlertService";
 import {findEntity} from "@/app/components/common/utils/ObjectUtils";
 import {ServicesContext} from "@/app/services/ServiceProvider";
 import {getRequestError} from "@/app/components/common/utils/RequestUtils";
 import ProductFilters from "@/app/components/product/ProductFilters";
 import {AuthServiceContext} from "@/app/services/AuthService";

type ProductListProps = {
  create?: (callback: () => void) => void,
  update?: (id: string, callback: () => void) => void,
  view?: (id: string) => void
};

export default function ProductList(props: ProductListProps): React.ReactNode {
  const { productService, productArchetypeService } = useContext(ServicesContext);
  const [items, setItems] = useState<Product[] | null>(null);
  const [criteria, setCriteria] = useState<ProductCriteria>(getDefaultBaseCriteria);
  const [productArchetypes, setProductArchetypes] = useState<ProductArchetype[] | null>(null);
  const showAlert = useContext(AlertContext);
  const authService = useContext(AuthServiceContext);

  useEffect(() => {
    const fetch = async() => {
      const response = await productArchetypeService.getProductArchetypeList({
        productArchetypeCriteria: {
          ids: items?.map(item => item.archetype) ?? []
        }
      });

      setProductArchetypes(response.items);
    };

    fetch().catch(e => getRequestError(e).then(m => showAlert(m, "error")));
  }, [items]);

  async function fetch(): Promise<ProductListResponse> {
    return await productService.getProductList({ productCriteria: criteria });
  }

  async function handleDelete(id: string) {
    return await productService.deleteProduct({ id });
  }

  function handleCreate(callback: () => void) {
    props.create?.(callback);
  }

  function handleView(id: string) {
    props.view?.(id);
  }

  function handleUpdate(id: string, callback: () => void) {
    props.update?.(id, callback);
  }

  const columns: GridColDef<Product>[] = [
    { field: "id", headerName: "UPC", width: 150 },
    {
      field: "archetype",
      headerName: "Назва",
      valueGetter: (value: number) => findEntity(productArchetypes, value)?.name ?? "",
      width: 300
    },
    {
      field: "hasDiscount",
      headerName: "Знижка",
      renderCell: ({ value }) => (<Checkbox checked={value ?? false} disableRipple />),
      width: 100
    },
    {
      field: "price",
      headerName: "Ціна",
      width: 150
    },
    {
      field: "quantity",
      headerName: "Кількість",
      width: 150
    }
  ];

  return (
    <ListComponent
      columns={columns}
      fetch={fetch}
      create={authService.hasRole(UserRole.Manager) ? handleCreate : undefined}
      view={handleView}
      update={authService.hasRole(UserRole.Manager) ? handleUpdate : undefined}
      delete={authService.hasRole(UserRole.Manager) ? handleDelete : undefined}
      criteria={criteria}
      setCriteria={setCriteria}

      items={items}
      setItems={setItems}

      filters={() => <ProductFilters criteria={criteria} setCriteria={setCriteria}/>}
    />
  );
}
