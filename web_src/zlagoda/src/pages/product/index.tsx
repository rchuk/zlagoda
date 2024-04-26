import {useRouter} from "next/router";
import ProductList from "@/app/components/product/ProductList";
import BasePage from "@/app/components/common/pages/BasePage";

export default function ProductListPage() {
  const router = useRouter();

  function create(callback: () => void) {
    router.push({
      pathname: "/product/create",
    });
  }

  function view(id: string) {
    router.push({
      pathname: "/product/[id]",
      query: { id }
    });
  }

  function update(id: string) {
    router.push({
      pathname: "/product/[id]/edit",
      query: { id }
    });
  }

  return (
    <BasePage>
      <ProductList
        create={create}
        view={view}
        update={update}
      />
    </BasePage>
  );
}
