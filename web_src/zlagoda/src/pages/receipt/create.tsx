import {useRouter} from "next/router";
import BasePage from "@/app/components/common/pages/BasePage";
import ReceiptCreate from "@/app/components/receipt/ReceiptCreate";

export default function ProductArchetypeCreatePage() {
  const router = useRouter();

  return (
    <BasePage>
      <ReceiptCreate cancel={router.back} onSave={router.back}/>
    </BasePage>
  )
}
