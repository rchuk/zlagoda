import {useRouter} from "next/router";
import EmployeeView from "@/app/components/employee/EmployeeView";
import {useContext, useState} from "react";
import BaseStringIdPage from "@/app/components/common/pages/BaseStringIdPage";
import {AuthServiceContext} from "@/app/services/AuthService";
import {UserRole} from "../../../../generated";

export default function EmployeeViewPage() {
  const [id, setId] = useState<string | null>(null);
  const router = useRouter();
  const authService = useContext(AuthServiceContext);

  function edit(id: string) {
    router.push({
      pathname: "/employee/[id]/edit",
      query: { id }
    })
  }

  return (
    <BaseStringIdPage id={id} setId={setId}>
      <EmployeeView id={id!} onError={router.back} edit={authService.hasRole(UserRole.Manager) ? edit : undefined} cancel={router.back}/>
    </BaseStringIdPage>
  );
}
