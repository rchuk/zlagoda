import {useContext, useState} from "react";
import BaseStringIdPage from "@/app/components/common/pages/BaseStringIdPage";
import {useRouter} from "next/router";
import ProductView from "@/app/components/product/ProductView";
import {AuthServiceContext} from "@/app/services/AuthService";
import {UserRole} from "../../../../generated";


export default function ProductViewPage() {
  const [id, setId] = useState<string | null>(null);
  const router = useRouter();
  const authService = useContext(AuthServiceContext);

  function edit(id: string) {
    router.push({
      pathname: "/product/[id]/edit",
      query: { id }
    })
  }

  return (
    <BaseStringIdPage id={id} setId={setId}>
      <ProductView id={id!} onError={router.back} edit={authService.hasRole(UserRole.Manager) ? edit : undefined} cancel={router.back}/>
    </BaseStringIdPage>
  );
}
