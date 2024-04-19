import {
  Employee,
  EmployeeApi,
  EmployeeCriteria,
  EmployeeListResponse, EmployeeRole
} from "../../../../generated";
import React, {useState} from "react";
import {Box} from "@mui/material";
import {GridColDef} from '@mui/x-data-grid';
import ListComponent, {getDefaultBaseCriteria} from "@/app/components/common/ListComponent";
import {EmployeeRole_i18} from "@/app/i18/EmployeeRole_i18";

type EmployeeListProps = {
  employeeService: EmployeeApi
};

export default function EmployeeList(props: EmployeeListProps): React.ReactNode {
  const [criteria, setCriteria] = useState<EmployeeCriteria>(getDefaultBaseCriteria);

  async function fetch(): Promise<EmployeeListResponse> {
    return {
      totalCount: 2,
      items: [
        { id: 1, firstName: "Валентин", lastName: "Нагорний", patronymic: "Миколайович", role: EmployeeRole.Cashier, salary: 15000, phoneNumber: "+380556029485",
          workStartDate: new Date(), birthDate: new Date(), zipCode: "04118", city: "Kyiv", street: "Some street"
        },
        { id: 3, firstName: "Андрій", lastName: "Запорожець", patronymic: "Батькович", role: EmployeeRole.Manager, salary: 25000, phoneNumber: "+380556024485",
          workStartDate: new Date(), birthDate: new Date(), zipCode: "04115", city: "Kyiv", street: "Different street"
        }
      ]
    };

    // return await props.employeeService.getEmployeeList({ employeeCriteria: criteria });
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
