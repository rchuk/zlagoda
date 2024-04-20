import {useState} from "react";
import BaseIdPage from "@/app/components/common/pages/BaseIdPage";
import {useRouter} from "next/router";
import ProductView from "@/app/components/product/ProductView";

export default function ProductViewPage() {
  const [id, setId] = useState<number | null>(null);
  const router = useRouter();

  return (
    <BaseIdPage id={id} setId={setId}>
      <ProductView id={id!} onError={router.back} cancel={router.back}/>
    </BaseIdPage>
  );
}
