import {useRouter} from "next/router";
import {useState} from "react";
import BaseIdPage from "@/app/components/common/pages/BaseIdPage";
import CustomerCardView from "@/app/components/customer-card/CustomerCardView";

export default function CustomerCardViewPage() {
  const [id, setId] = useState<number | null>(null);
  const router = useRouter();

  function edit(id: number) {
    router.push({
      pathname: "/customer-card/[id]/edit",
      query: { id }
    })
  }

  return (
    <BaseIdPage id={id} setId={setId}>
      <CustomerCardView id={id!} onError={router.back} edit={edit} cancel={router.back}/>
    </BaseIdPage>
  );
}
