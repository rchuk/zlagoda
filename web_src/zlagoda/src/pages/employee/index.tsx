import EmployeeList from "@/app/components/employee/EmployeeList";
import {useRouter} from "next/router";
import BasePage from "@/app/components/common/pages/BasePage";

export default function EmployeeListPage() {
  const router = useRouter();

  function create(callback: () => void) {
    router.push({
      pathname: "/employee/create",
    });
  }

  function view(id: number) {
    router.push({
      pathname: "/employee/[id]",
      query: { id }
    });
  }

  function update(id: number) {
    router.push({
      pathname: "/employee/[id]/edit",
      query: { id }
    });
  }

  return (
    <BasePage>
      <EmployeeList
        create={create}
        view={view}
        update={update}
      />
    </BasePage>
  );
}
