import {
  ProductArchetype,
  ProductArchetypeCriteria,
  ProductArchetypeListResponse, ProductCategory
} from "../../../../generated";
import React, {useContext, useEffect, useState} from "react";
import {Box} from "@mui/material";
import {GridColDef} from '@mui/x-data-grid';
import ListComponent, {getDefaultBaseCriteria} from "@/app/components/common/ListComponent";
import {AlertContext} from "@/app/services/AlertService";
import {createIdsCriteria, findEntity} from "@/app/components/common/utils/ObjectUtils";
import {ServicesContext} from "@/app/services/ServiceProvider";

type ProductArchetypeListProps = {

};

export default function ProductArchetypeList(props: ProductArchetypeListProps): React.ReactNode {
  const { productArchetypeService, productCategoryService } = useContext(ServicesContext);
  const [items, setItems] = useState<ProductArchetype[] | null>(null);
  const [criteria, setCriteria] = useState<ProductArchetypeCriteria>(getDefaultBaseCriteria);
  const [productCategories, setProductCategories] = useState<ProductCategory[] | null>(null);
  const showAlert = useContext(AlertContext);

  useEffect(() => {
    const fetch = async() => {
      const response = await productCategoryService.getProductCategoryList({
        productCategoryCriteria: createIdsCriteria(items)
      });

      setProductCategories(response.items);
    };

    fetch().catch(e => showAlert(e.toString(), "error"));
  }, [items]);

  async function fetch(): Promise<ProductArchetypeListResponse> {
    return await productArchetypeService.getProductArchetypeList({ productArchetypeCriteria: criteria });
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
      valueGetter: value => findEntity(productCategories, value)?.name ?? "",
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
