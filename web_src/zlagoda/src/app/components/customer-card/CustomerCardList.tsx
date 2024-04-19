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

};

export default function CustomerCardList(props: CustomerCardListProps): React.ReactNode {
  const { customerCardService } = useContext(ServicesContext);
  const [criteria, setCriteria] = useState<CustomerCardCriteria>(getDefaultBaseCriteria);

  async function fetch(): Promise<CustomerCardListResponse> {
    return {
      totalCount: 2,
      items: [
        { id: 0, firstName: "Валентин", lastName: "Нагорний", patronymic: "Миколайович", discountPercent: 10, phoneNumber: "+380556029485" },
        { id: 3, firstName: "Андрій", lastName: "Запорожець", discountPercent: 12, phoneNumber: "+380556024485" }
      ]
    };

    // return await customerCardService.getCustomerCardList({ customerCardCriteria: criteria });
  }

  function handleCreate(callback: () => void) {

  }

  function handleView(id: number) {

  }

  function handleUpdate(id: number) {

  }

  function handleDelete(id: number, callback: () => void) {

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
      />
    </Box>
  );
}
