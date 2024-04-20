import {
  ProductCategory,
  ProductCategoryCriteria,
  ProductCategoryListResponse
} from "../../../../generated";
import React, {useContext, useState} from "react";
import {Box} from "@mui/material";
import {GridColDef} from '@mui/x-data-grid';
import ListComponent, {getDefaultBaseCriteria} from "@/app/components/common/ListComponent";
import {ServicesContext} from "@/app/services/ServiceProvider";

type ProductCategoryListProps = {
  create?: (callback: () => void) => void,
  update?: (id: number) => void
};

export default function ProductCategoryList(props: ProductCategoryListProps): React.ReactNode {
  const { productCategoryService } = useContext(ServicesContext);
  const [criteria, setCriteria] = useState<ProductCategoryCriteria>(getDefaultBaseCriteria);

  async function fetch(): Promise<ProductCategoryListResponse> {
    return await productCategoryService.getProductCategoryList({ productCategoryCriteria: criteria });
  }

  async function handleDelete(id: number) {
    return await productCategoryService.deleteProductCategory({ id });
  }

  function handleCreate(callback: () => void) {
    props.create?.(callback);
  }

  function handleUpdate(id: number) {
    props.update?.(id);
  }

  const columns: GridColDef<ProductCategory>[] = [
    { field: "id", headerName: "ID", width: 80 },
    {
      field: "name",
      headerName: 'Назва',
      width: 300
    }
  ];

  // TODO: Handle filters

  return (
    <Box>
      <ListComponent
        columns={columns}
        fetch={fetch}
        create={handleCreate}
        update={handleUpdate}
        delete={handleDelete}
        criteria={criteria}
        setCriteria={setCriteria}
      />
    </Box>
  );
}
