import {useRouter} from "next/router";
import {useState} from "react";
import EmployeeUpsert from "@/app/components/employee/EmployeeUpsert";
import BaseStringIdPage from "@/app/components/common/pages/BaseStringIdPage";

export default function EmployeeEditPage() {
  const [id, setId] = useState<string | null>(null);
  const router = useRouter();

  return (
    <BaseStringIdPage id={id} setId={setId}>
      <EmployeeUpsert initialId={id} onError={router.back} cancel={router.back} onSave={router.back}/>
    </BaseStringIdPage>
  );
}
