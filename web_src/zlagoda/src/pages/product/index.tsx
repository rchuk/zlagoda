import {useRouter} from "next/router";
import ProductList from "@/app/components/product/ProductList";
import {Box} from "@mui/material";

export default function ProductListPage() {
  const router = useRouter();

  function create(callback: () => void) {
    router.push({
      pathname: "/product/create",
    });
  }

  function view(id: number) {
    router.push({
      pathname: "/product/[id]",
      query: { id }
    });
  }

  function update(id: number) {
    router.push({
      pathname: "/product/[id]/edit",
      query: { id }
    });
  }

  return (
    <Box>
      <ProductList
        create={create}
        view={view}
        update={update}
      />
    </Box>
  );
}
