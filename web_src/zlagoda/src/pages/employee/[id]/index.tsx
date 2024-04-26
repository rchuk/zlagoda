import {useRouter} from "next/router";
import EmployeeView from "@/app/components/employee/EmployeeView";
import {useState} from "react";
import BaseStringIdPage from "@/app/components/common/pages/BaseStringIdPage";

export default function EmployeeViewPage() {
  const [id, setId] = useState<string | null>(null);
  const router = useRouter();

  function edit(id: string) {
    router.push({
      pathname: "/employee/[id]/edit",
      query: { id }
    })
  }

  return (
    <BaseStringIdPage id={id} setId={setId}>
      <EmployeeView id={id!} onError={router.back} edit={edit} cancel={router.back}/>
    </BaseStringIdPage>
  );
}
