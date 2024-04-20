import {useRouter} from "next/router";
import {useState} from "react";
import EmployeeUpsert from "@/app/components/employee/EmployeeUpsert";
import BaseIdPage from "@/app/components/common/pages/BaseIdPage";

export default function EmployeeEditPage() {
  const [id, setId] = useState<number | null>(null);
  const router = useRouter();

  return (
    <BaseIdPage id={id} setId={setId}>
      <EmployeeUpsert initialId={id} onError={router.back} cancel={router.back}/>
    </BaseIdPage>
  );
}
