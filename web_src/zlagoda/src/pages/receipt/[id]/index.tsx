import {useState} from "react";
import {useRouter} from "next/router";
import ReceiptView from "@/app/components/receipt/ReceiptView";
import BaseStringIdPage from "@/app/components/common/pages/BaseStringIdPage";

export default function ReceiptViewPage() {
  const [id, setId] = useState<string | null>(null);
  const router = useRouter();

  return (
    <BaseStringIdPage id={id} setId={setId}>
      <ReceiptView id={id!} onError={router.back} cancel={router.back} />
    </BaseStringIdPage>
  );
}
