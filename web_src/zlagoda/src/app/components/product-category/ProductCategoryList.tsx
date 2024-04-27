import {
  ProductCategory,
  ProductCategoryCriteria,
  ProductCategoryListResponse, UserRole
} from "../../../../generated";
import React, {useContext, useState} from "react";
import {GridColDef} from '@mui/x-data-grid';
import ListComponent, {getDefaultBaseCriteria} from "@/app/components/common/ListComponent";
import {ServicesContext} from "@/app/services/ServiceProvider";
import {AuthServiceContext} from "@/app/services/AuthService";

type ProductCategoryListProps = {
  create?: (callback: () => void) => void,
  update?: (id: number, callback: () => void) => void
};

export default function ProductCategoryList(props: ProductCategoryListProps): React.ReactNode {
  const { productCategoryService } = useContext(ServicesContext);
  const [criteria, setCriteria] = useState<ProductCategoryCriteria>(getDefaultBaseCriteria);
  const authService = useContext(AuthServiceContext);

  async function fetch(): Promise<ProductCategoryListResponse> {
    return await productCategoryService.getProductCategoryList({ productCategoryCriteria: criteria });
  }

  async function handleDelete(id: number) {
    return await productCategoryService.deleteProductCategory({ id });
  }

  function handleCreate(callback: () => void) {
    props.create?.(callback);
  }

  function handleUpdate(id: number, callback: () => void) {
    props.update?.(id, callback);
  }

  const columns: GridColDef<ProductCategory>[] = [
    { field: "id", headerName: "ID", width: 80 },
    {
      field: "name",
      headerName: 'Назва',
      width: 350
    }
  ];

  // TODO: Handle filters

  return (
    <ListComponent
      columns={columns}
      fetch={fetch}
      create={authService.hasRole(UserRole.Manager) ? handleCreate : undefined}
      update={authService.hasRole(UserRole.Manager) ? handleUpdate : undefined}
      delete={authService.hasRole(UserRole.Manager) ? handleDelete : undefined}
      criteria={criteria}
      setCriteria={setCriteria}
    />
  );
}
