import {
  CustomerCard,
  CustomerCardCriteria,
  CustomerCardListResponse, UserRole
} from "../../../../generated";
import React, {useContext, useState} from "react";
import {GridColDef} from '@mui/x-data-grid';
import ListComponent, {getDefaultBaseCriteria} from "@/app/components/common/ListComponent";
import {ServicesContext} from "@/app/services/ServiceProvider";
import CustomerCardFilters from "@/app/components/customer-card/CustomerCardFilters";
import {AuthServiceContext} from "@/app/services/AuthService";

type CustomerCardListProps = {
    create?: (callback: () => void) => void,
    update?: (id: string, callback: () => void) => void
    view?: (id: string) => void
};

export default function CustomerCardList(props: CustomerCardListProps): React.ReactNode {
  const { customerCardService } = useContext(ServicesContext);
  const [criteria, setCriteria] = useState<CustomerCardCriteria>(getDefaultBaseCriteria);
  const authService = useContext(AuthServiceContext);

  async function fetch(): Promise<CustomerCardListResponse> {
    return await customerCardService.getCustomerCardList({ customerCardCriteria: criteria });
  }

  async function handleDelete(id: string) {
    return await customerCardService.deleteCustomerCard({ id });
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

  const columns: GridColDef<CustomerCard>[] = [
    {
      field: "id",
      headerName: "ID",
      width: 120
    },
    {
      field: "lastName",
      headerName: "Прізвище",
      width: 200
    },
    {
      field: "firstName",
      headerName: "Ім'я",
      width: 200
    },
    {
      field: "patronymic",
      headerName: "По-батькові",
      width: 200
    },
    {
      field: "discountPercent",
      headerName: "Знижка",
      width: 150
    },
    {
      field: "phoneNumber",
      headerName: "Номер телефону",
      width: 150
    }
  ];

  return (
    <ListComponent
      columns={columns}
      fetch={fetch}
      create={authService.hasRole(UserRole.Manager) ? handleCreate : undefined}
      view={handleView}
      update={handleUpdate}
      delete={authService.hasRole(UserRole.Manager) ? handleDelete : undefined}
      criteria={criteria}
      setCriteria={setCriteria}

      filters={() => <CustomerCardFilters criteria={criteria} setCriteria={setCriteria} />}
    />
  );
}
