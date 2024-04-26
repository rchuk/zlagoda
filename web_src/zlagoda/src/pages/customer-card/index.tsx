import {useRouter} from "next/router";
import CustomerCardList from "@/app/components/customer-card/CustomerCardList";
import BasePage from "@/app/components/common/pages/BasePage";


export default function CustomerCardListPage() {
  const router = useRouter();

  function create(callback: () => void) {
    router.push({
      pathname: "/customer-card/create",
    });
  }

  function view(id: string) {
    router.push({
      pathname: "/customer-card/[id]",
      query: { id }
    });
  }

  function update(id: string) {
    router.push({
      pathname: "/customer-card/[id]/edit",
      query: { id }
    });
  }

  return (
    <BasePage>
      <CustomerCardList
        create={create}
        view={view}
        update={update}
      />
    </BasePage>
  );
}
