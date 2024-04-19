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

};

export default function ProductCategoryList(props: ProductCategoryListProps): React.ReactNode {
  const { productCategoryService } = useContext(ServicesContext);
  const [criteria, setCriteria] = useState<ProductCategoryCriteria>(getDefaultBaseCriteria);

  async function fetch(): Promise<ProductCategoryListResponse> {
    return {
      totalCount: 2,
      items: [
        { id: 0, name: "Тест" },
        { id: 1, name: "Бла бла" }
      ]
    };

    // return await productCategoryService.getProductCategoryList({ productCategoryCriteria: criteria });
  }

  function handleCreate(callback: () => void) {

  }

  function handleUpdate(id: number) {

  }

  function handleDelete(id: number, callback: () => void) {

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
