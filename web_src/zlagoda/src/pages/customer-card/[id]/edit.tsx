import {useRouter} from "next/router";
import {useState} from "react";
import BaseIdPage from "@/app/components/common/pages/BaseIdPage";
import CustomerCardUpsert from "@/app/components/customer-card/CustomerCardUpsert";

export default function CustomerCardEditPage() {
  const [id, setId] = useState<number | null>(null);
  const router = useRouter();

  return (
    <BaseIdPage id={id} setId={setId}>
      <CustomerCardUpsert initialId={id} onError={router.back} cancel={router.back}/>
    </BaseIdPage>
  );
}
