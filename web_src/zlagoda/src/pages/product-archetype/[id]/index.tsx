import {useState} from "react";
import ProgressSpinner from "@/app/components/common/ProgressSpinner";
import ProductArchetypeView from "@/app/components/product-archetype/ProductArchetypeView";
import BaseIdPage from "@/app/components/common/pages/BaseIdPage";
import {useRouter} from "next/router";

export default function ProductArchetypeViewPage() {
  const [id, setId] = useState<number | null>(null);
  const router = useRouter();

  return (
    <BaseIdPage id={id} setId={setId}>
      <ProductArchetypeView id={id!} onError={router.back} cancel={router.back}/>
    </BaseIdPage>
  );
}
