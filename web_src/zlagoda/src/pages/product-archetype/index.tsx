import ProductArchetypeList from "@/app/components/product-archetype/ProductArchetypeList";
import {useRouter} from "next/router";

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
    <ProductArchetypeList
      create={create}
      view={view}
      update={update}
    />
  );
}
