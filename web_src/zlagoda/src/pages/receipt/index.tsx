import {useRouter} from "next/router";
import ReceiptList from "@/app/components/receipt/ReceiptList";
import BasePage from "@/app/components/common/pages/BasePage";

export default function ReceiptListPage() {
  const router = useRouter();

  function create(callback: () => void) {
    router.push({
      pathname: "/receipt/create",
    });
  }

  function view(id: string) {
    router.push({
      pathname: "/receipt/[id]",
      query: { id }
    });
  }

  return (
    <BasePage>
      <ReceiptList
        create={create}
        view={view}
      />
    </BasePage>
  );
}
