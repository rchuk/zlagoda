import {useState} from "react";
import BaseStringIdPage from "@/app/components/common/pages/BaseStringIdPage";
import {useRouter} from "next/router";
import ProductView from "@/app/components/product/ProductView";


export default function ProductViewPage() {
  const [id, setId] = useState<string | null>(null);
  const router = useRouter();

  function edit(id: string) {
    router.push({
      pathname: "/product/[id]/edit",
      query: { id }
    })
  }

  return (
    <BaseStringIdPage id={id} setId={setId}>
      <ProductView id={id!} onError={router.back} edit={edit} cancel={router.back}/>
    </BaseStringIdPage>
  );
}
