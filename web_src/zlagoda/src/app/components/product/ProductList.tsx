 import {
  Product,
  ProductArchetype,
  ProductCriteria,
  ProductListResponse
} from "../../../../generated";
import React, {useContext, useEffect, useState} from "react";
import {Box, Checkbox} from "@mui/material";
import {GridColDef} from '@mui/x-data-grid';
import ListComponent, {getDefaultBaseCriteria} from "@/app/components/common/ListComponent";
 import {AlertContext} from "@/app/services/AlertService";
 import {createIdsCriteria, findEntity} from "@/app/components/common/utils/ObjectUtils";
 import {ServicesContext} from "@/app/services/ServiceProvider";

type ProductListProps = {
  create?: (callback: () => void) => void,
  update?: (id: number, callback: () => void) => void,
  view?: (id: number) => void
};

export default function ProductList(props: ProductListProps): React.ReactNode {
  const { productService, productArchetypeService } = useContext(ServicesContext);
  const [items, setItems] = useState<Product[] | null>(null);
  const [criteria, setCriteria] = useState<ProductCriteria>(getDefaultBaseCriteria);
  const [productArchetypes, setProductArchetypes] = useState<ProductArchetype[] | null>(null);
  const showAlert = useContext(AlertContext);

  useEffect(() => {
    const fetch = async() => {
      const response = await productArchetypeService.getProductArchetypeList({
        productArchetypeCriteria: createIdsCriteria(items)
      });

      setProductArchetypes(response.items);
    };

    fetch().catch(e => showAlert(e.toString(), "error"));
  }, [items]);

  async function fetch(): Promise<ProductListResponse> {
    return await productService.getProductList({ productCriteria: criteria });
  }

  async function handleDelete(id: number) {
    return await productService.deleteProduct({ id });
  }

  function handleCreate(callback: () => void) {
    props.create?.(callback);
  }

  function handleView(id: number) {
    props.view?.(id);
  }

  function handleUpdate(id: number, callback: () => void) {
    props.update?.(id, callback);
  }

  const columns: GridColDef<Product>[] = [
    { field: "id", headerName: "ID", width: 80 },
    {
      field: "archetype",
      headerName: "Назва",
      valueGetter: value => findEntity(productArchetypes, value)?. name ?? "",
      width: 300
    },
    {
      field: "upc",
      headerName: "UPC",
      width: 200
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

  // TODO: Handle filters

  return (
    <ListComponent
      columns={columns}
      fetch={fetch}
      create={handleCreate}
      view={handleView}
      update={handleUpdate}
      delete={handleDelete}
      criteria={criteria}
      setCriteria={setCriteria}

      items={items}
      setItems={setItems}
    />
  );
}
