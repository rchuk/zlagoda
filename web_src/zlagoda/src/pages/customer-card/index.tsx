import {useRouter} from "next/router";
import CustomerCardList from "@/app/components/customer-card/CustomerCardList";

export default function CustomerCardListPage() {
  const router = useRouter();

  function create(callback: () => void) {
    router.push({
      pathname: "/customer-card/create",
    });
  }

  function view(id: number) {
    router.push({
      pathname: "/customer-card/[id]",
      query: { id }
    });
  }

  function update(id: number) {
    router.push({
      pathname: "/customer-card/[id]/edit",
      query: { id }
    });
  }

  return (
    <CustomerCardList
      create={create}
      view={view}
      update={update}
    />
  );
}
