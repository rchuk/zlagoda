import {useRouter} from "next/router";
import EmployeeUpsert from "@/app/components/employee/EmployeeUpsert";
import BasePage from "@/app/components/common/pages/BasePage";

export default function EmployeeCreatePage() {
  const router = useRouter();

  return (
    <BasePage>
      <EmployeeUpsert initialId={null} onError={router.back} cancel={router.back}/>
    </BasePage>
  )
}
