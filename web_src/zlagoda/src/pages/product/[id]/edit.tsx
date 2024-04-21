import {useRouter} from "next/router";
import {useState} from "react";
import BaseStringIdPage from "@/app/components/common/pages/BaseStringIdPage";
import ProductUpsert from "@/app/components/product/ProductUpsert";

export default function ProductEditPage() {
  const [id, setId] = useState<string | null>(null);
  const router = useRouter();

  return (
    <BaseStringIdPage id={id} setId={setId}>
      <ProductUpsert initialId={id} onError={router.back} cancel={router.back} onSave={router.back}/>
    </BaseStringIdPage>
  );
}
