import {useRouter} from "next/router";
import EmployeeView from "@/app/components/employee/EmployeeView";
import {useState} from "react";
import BaseIdPage from "@/app/components/common/pages/BaseIdPage";

export default function EmployeeViewPage() {
  const [id, setId] = useState<number | null>(null);
  const router = useRouter();

  function edit(id: number) {
    router.push({
      pathname: "/employee/[id]/edit",
      query: { id }
    })
  }

  return (
    <BaseIdPage id={id} setId={setId}>
      <EmployeeView id={id!} onError={router.back} edit={edit} cancel={router.back}/>
    </BaseIdPage>
  );
}
