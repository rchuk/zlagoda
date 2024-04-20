import {useRouter} from "next/router";
import BasePage from "@/app/components/common/pages/BasePage";
import CustomerCardUpsert from "@/app/components/customer-card/CustomerCardUpsert";

export default function CustomerCardCreatePage() {
  const router = useRouter();

  return (
    <BasePage>
      <CustomerCardUpsert initialId={null} onError={router.back} cancel={router.back}/>
    </BasePage>
  )
}
