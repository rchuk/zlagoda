import {useRouter} from "next/router";
import {useContext, useState} from "react";
import CustomerCardView from "@/app/components/customer-card/CustomerCardView";
import BaseStringIdPage from "@/app/components/common/pages/BaseStringIdPage";
import {AuthServiceContext} from "@/app/services/AuthService";

export default function CustomerCardViewPage() {
  const [id, setId] = useState<string | null>(null);
  const router = useRouter();

  function edit(id: string) {
    router.push({
      pathname: "/customer-card/[id]/edit",
      query: { id }
    })
  }

  return (
    <BaseStringIdPage id={id} setId={setId}>
      <CustomerCardView id={id!} onError={router.back} edit={edit} cancel={router.back}/>
    </BaseStringIdPage>
  );
}
