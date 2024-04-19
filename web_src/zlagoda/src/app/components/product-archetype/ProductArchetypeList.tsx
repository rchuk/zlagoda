import {
  ProductArchetype,
  ProductArchetypeApi,
  ProductArchetypeCriteria,
  ProductArchetypeListResponse, ProductCategory, ProductCategoryApi
} from "../../../../generated";
import React, {useContext, useEffect, useState} from "react";
import {Box} from "@mui/material";
import {GridColDef} from '@mui/x-data-grid';
import ListComponent, {getDefaultBaseCriteria} from "@/app/components/common/ListComponent";
import {AlertContext} from "@/app/services/AlertService";

type ProductArchetypeListProps = {
  productArchetypeService: ProductArchetypeApi,
  productCategoryService: ProductCategoryApi
};

export default function ProductArchetypeList(props: ProductArchetypeListProps): React.ReactNode {
  const [items, setItems] = useState<ProductArchetype[] | null>(null);
  const [criteria, setCriteria] = useState<ProductArchetypeCriteria>(getDefaultBaseCriteria);
  const [productCategories, setProductCategories] = useState<ProductCategory[] | null>(null);
  const showAlert = useContext(AlertContext);

  useEffect(() => {
    const fetch = async() => {
      const response = await props.productCategoryService.getProductCategoryList({
        productCategoryCriteria: {
          ids: items?.map(item => item.id) ?? []
        }
      });

      setProductCategories(response.items);
    };

    fetch().catch(e => showAlert(e.toString(), "error"));
  }, [items]);

  async function fetch(): Promise<ProductArchetypeListResponse> {
    return {
      totalCount: 2,
      items: [
        { id: 0, name: "Щось", category: 0, manufacturer: "Київський Завод ЛХБЧ", description: "asfasf" },
        { id: 1, name: "Бла бла", category: 4, manufacturer: "Харківський КМСБ", description: "dgkdkgkd" }
      ]
    };

    // return await props.productArchetypeService.getProductArchetypeList({ productArchetypeCriteria: criteria });
  }

  function handleCreate(callback: () => void) {

  }

  function handleView(id: number) {

  }

  function handleUpdate(id: number) {

  }

  function handleDelete(id: number, callback: () => void) {

  }

  const columns: GridColDef<ProductArchetype>[] = [
    { field: "id", headerName: "ID", width: 80 },
    {
      field: "name",
      headerName: "Назва",
      width: 300
    },
    {
      field: "category",
      headerName: "Категорія",
      valueGetter: value => {
        return productCategories?.find(category => category.id == value)?.name ?? "";
      },
      width: 200
    },
    {
      field: "manufacturer",
      headerName: "Виробник",
      width: 200
    }
  ];

  // TODO: Handle filters

  return (
    <Box>
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
    </Box>
  );
}
