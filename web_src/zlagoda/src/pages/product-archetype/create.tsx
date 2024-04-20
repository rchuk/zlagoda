import {useRouter} from "next/router";
import BasePage from "@/app/components/common/pages/BasePage";
import ProductArchetypeUpsert from "@/app/components/product-archetype/ProductArchetypeUpsert";

export default function ProductArchetypeCreatePage() {
  const router = useRouter();

  return (
    <BasePage>
      <ProductArchetypeUpsert initialId={null} onError={router.back} cancel={router.back}/>
    </BasePage>
  )
}
