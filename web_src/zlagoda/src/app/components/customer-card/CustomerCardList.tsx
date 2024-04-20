import {
  CustomerCard,
  CustomerCardCriteria,
  CustomerCardListResponse
} from "../../../../generated";
import React, {useContext, useState} from "react";
import {Box} from "@mui/material";
import {GridColDef} from '@mui/x-data-grid';
import ListComponent, {getDefaultBaseCriteria} from "@/app/components/common/ListComponent";
import {ServicesContext} from "@/app/services/ServiceProvider";

type CustomerCardListProps = {
    create?: (callback: () => void) => void,
    update?: (id: number) => void,
    view?: (id: number) => void
};

export default function CustomerCardList(props: CustomerCardListProps): React.ReactNode {
  const { customerCardService } = useContext(ServicesContext);
  const [criteria, setCriteria] = useState<CustomerCardCriteria>(getDefaultBaseCriteria);

  async function fetch(): Promise<CustomerCardListResponse> {
    return await customerCardService.getCustomerCardList({ customerCardCriteria: criteria });
  }

  async function handleDelete(id: number) {
    return await customerCardService.deleteCustomerCard({ id });
  }

  function handleCreate(callback: () => void) {
    props.create?.(callback);
  }

  function handleView(id: number) {
    props.view?.(id);
  }

  function handleUpdate(id: number) {
    props.update?.(id);
  }

  const columns: GridColDef<CustomerCard>[] = [
    { field: "id", headerName: "ID", width: 80 },
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
    />
  );
}
