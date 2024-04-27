import ApiAutocompleteComponent from "@/app/components/common/autocomplete/ApiAutocompleteComponent";
import {BaseCriteria, Employee} from "../../../../../generated";
import {useContext} from "react";
import {ServicesContext} from "@/app/services/ServiceProvider";
import {getEntityPersonFullName} from "@/app/components/common/utils/BusinessUtils";


type EmployeeAutocompleteProps = {
  initialId?: string,
  setSelectedId: (value: string | null) => void
};

export default function EmployeeAutocomplete(props: EmployeeAutocompleteProps) {
  const { employeeService } = useContext(ServicesContext);

  async function fetch(criteria: BaseCriteria) {
    return await employeeService.getEmployeeList({ employeeCriteria: criteria });
  }

  return (
    <ApiAutocompleteComponent
      initialId={props.initialId}
      setSelectedId={props.setSelectedId}
      fetch={fetch}
      label={"Працівник"}
      getItemLabel={(item: Employee) => getEntityPersonFullName(item)}
    />
  );
}
