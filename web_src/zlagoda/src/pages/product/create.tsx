import {useRouter} from "next/router";
import BasePage from "@/app/components/common/pages/BasePage";
import ProductUpsert from "@/app/components/product/ProductUpsert";

export default function ProductCreatePage() {
  const router = useRouter();

  return (
    <BasePage>
      <ProductUpsert initialId={null} onError={router.back} cancel={router.back}/>
    </BasePage>
  )
}
