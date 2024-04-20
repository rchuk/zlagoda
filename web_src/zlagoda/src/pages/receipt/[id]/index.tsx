import {useState} from "react";
import BaseIdPage from "@/app/components/common/pages/BaseIdPage";
import {useRouter} from "next/router";
import ReceiptView from "@/app/components/receipt/ReceiptView";

export default function ReceiptViewPage() {
  const [id, setId] = useState<number | null>(null);
  const router = useRouter();

  return (
    <BaseIdPage id={id} setId={setId}>
      <ReceiptView id={id!} onError={router.back} cancel={router.back}/>
    </BaseIdPage>
  );
}
