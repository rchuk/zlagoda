import {useRouter} from "next/router";
import {useState} from "react";
import BaseStringIdPage from "@/app/components/common/pages/BaseStringIdPage";
import ProductUpsert from "@/app/components/product/ProductUpsert";

export default function ProductEditPage() {
  const [id, setId] = useState<string | null>(null);
  const router = useRouter();

  function onSave(id?: string) {
    if (id) {
      router.replace({
        pathname: "/product/[id]",
        query: id
      })
    }
  }

  return (
    <BaseStringIdPage id={id} setId={setId}>
      <ProductUpsert initialId={id} onError={router.back} cancel={router.back} onSave={onSave}/>
    </BaseStringIdPage>
  );
}
