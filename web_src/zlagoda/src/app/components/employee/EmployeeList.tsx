import {
  Employee,
  EmployeeCriteria,
  EmployeeListResponse
} from "../../../../generated";
import React, {useContext, useState} from "react";
import {GridColDef} from '@mui/x-data-grid';
import ListComponent, {getDefaultBaseCriteria} from "@/app/components/common/ListComponent";
import {EmployeeRole_i18} from "@/app/i18/EmployeeRole_i18";
import {ServicesContext} from "@/app/services/ServiceProvider";
import EmployeeFilters from "./EmployeeFilters";

type EmployeeListProps = {
  create?: (callback: () => void) => void,
  update?: (id: string, callback: () => void) => void,
  view?: (id: string) => void
};

export default function EmployeeList(props: EmployeeListProps): React.ReactNode {
  const { employeeService } = useContext(ServicesContext);
  const [criteria, setCriteria] = useState<EmployeeCriteria>(getDefaultBaseCriteria);

  async function fetch(): Promise<EmployeeListResponse> {
    return await employeeService.getEmployeeList({ employeeCriteria: criteria });
  }

  async function handleDelete(id: string) {
    return await employeeService.deleteEmployee({ id });
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

  const columns: GridColDef<Employee>[] = [
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
      filters={() => <EmployeeFilters criteria={criteria} setCriteria={setCriteria} />}
      setQuery={(query) => setCriteria({...criteria, query})}
    />
  );
}
