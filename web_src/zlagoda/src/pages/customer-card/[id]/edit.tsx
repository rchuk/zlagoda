import {useRouter} from "next/router";
import {useState} from "react";
import CustomerCardUpsert from "@/app/components/customer-card/CustomerCardUpsert";
import BaseStringIdPage from "@/app/components/common/pages/BaseStringIdPage";

export default function CustomerCardEditPage() {
  const [id, setId] = useState<string | null>(null);
  const router = useRouter();

  return (
    <BaseStringIdPage id={id} setId={setId}>
      <CustomerCardUpsert initialId={id} onError={router.back} cancel={router.back} onSave={router.back} />
    </BaseStringIdPage>
  );
}
