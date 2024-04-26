import ProductArchetypeList from "@/app/components/product-archetype/ProductArchetypeList";
import {useRouter} from "next/router";
import BasePage from "@/app/components/common/pages/BasePage";

export default function ProductArchetypeListPage() {
  const router = useRouter();

  function create(callback: () => void) {
    router.push({
      pathname: "/product-archetype/create",
    });
  }

  function view(id: number) {
    router.push({
      pathname: "/product-archetype/[id]",
      query: { id }
    });
  }

  function update(id: number) {
    router.push({
      pathname: "/product-archetype/[id]/edit",
      query: { id }
    });
  }

  return (
    <BasePage>
      <ProductArchetypeList
        create={create}
        view={view}
        update={update}
      />
    </BasePage>
  );
}
