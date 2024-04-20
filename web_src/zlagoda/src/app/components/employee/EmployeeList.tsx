import {
  Employee,
  EmployeeCriteria,
  EmployeeListResponse
} from "../../../../generated";
import React, {useContext, useState} from "react";
import {Box} from "@mui/material";
import {GridColDef} from '@mui/x-data-grid';
import ListComponent, {getDefaultBaseCriteria} from "@/app/components/common/ListComponent";
import {EmployeeRole_i18} from "@/app/i18/EmployeeRole_i18";
import {ServicesContext} from "@/app/services/ServiceProvider";
import {useRouter} from "next/router";

type EmployeeListProps = {

};

export default function EmployeeList(props: EmployeeListProps): React.ReactNode {
  const { employeeService } = useContext(ServicesContext);
  const [criteria, setCriteria] = useState<EmployeeCriteria>(getDefaultBaseCriteria);

  async function fetch(): Promise<EmployeeListResponse> {
    return await employeeService.getEmployeeList({ employeeCriteria: criteria });
  }

  function handleCreate(callback: () => void) {

  }

  function handleView(id: number) {

  }

  function handleUpdate(id: number) {

  }

  function handleDelete(id: number, callback: () => void) {

  }

  const columns: GridColDef<Employee>[] = [
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
      field: "role",
      headerName: "Посада",
      valueGetter: value => EmployeeRole_i18[value],
      width: 150
    },
    {
      field: "salary",
      headerName: "Зарплатня",
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
