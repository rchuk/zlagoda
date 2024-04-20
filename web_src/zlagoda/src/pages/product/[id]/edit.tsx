import {useRouter} from "next/router";
import {useState} from "react";
import BaseIdPage from "@/app/components/common/pages/BaseIdPage";
import ProductUpsert from "@/app/components/product/ProductUpsert";

export default function ProductEditPage() {
  const [id, setId] = useState<number | null>(null);
  const router = useRouter();

  return (
    <BaseIdPage id={id} setId={setId}>
      <ProductUpsert initialId={id} onError={router.back} cancel={router.back}/>
    </BaseIdPage>
  );
}
