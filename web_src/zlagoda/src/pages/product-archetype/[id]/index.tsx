import {useContext, useState} from "react";
import ProgressSpinner from "@/app/components/common/ProgressSpinner";
import ProductArchetypeView from "@/app/components/product-archetype/ProductArchetypeView";
import BaseIdPage from "@/app/components/common/pages/BaseIdPage";
import {useRouter} from "next/router";
import {AuthServiceContext} from "@/app/services/AuthService";
import {UserRole} from "../../../../generated";

export default function ProductArchetypeViewPage() {
  const [id, setId] = useState<number | null>(null);
  const router = useRouter();
  const authService = useContext(AuthServiceContext);

  function edit(id: number) {
    router.push({
      pathname: "/product-archetype/[id]/edit",
      query: { id }
    })
  }

  return (
    <BaseIdPage id={id} setId={setId}>
      <ProductArchetypeView id={id!} onError={router.back} edit={authService.hasRole(UserRole.Manager) ? edit : undefined} cancel={router.back}/>
    </BaseIdPage>
  );
}
