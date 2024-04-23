import {useRouter} from "next/router";
import {useState} from "react";
import BaseIdPage from "@/app/components/common/pages/BaseIdPage";
import ProductArchetypeUpsert from "@/app/components/product-archetype/ProductArchetypeUpsert";

export default function ProductArchetypeEditPage() {
  const [id, setId] = useState<number | null>(null);
  const router = useRouter();

  return (
    <BaseIdPage id={id} setId={setId}>
      <ProductArchetypeUpsert initialId={id} onError={router.back} cancel={router.back} onSave={router.back}/>
    </BaseIdPage>
  );
}
