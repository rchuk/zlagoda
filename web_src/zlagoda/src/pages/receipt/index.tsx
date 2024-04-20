import {useRouter} from "next/router";
import ReceiptList from "@/app/components/receipt/ReceiptList";

export default function ReceiptListPage() {
  const router = useRouter();

  function create(callback: () => void) {
    router.push({
      pathname: "/receipt/create",
    });
  }

  function view(id: number) {
    router.push({
      pathname: "/receipt/[id]",
      query: { id }
    });
  }

  function update(id: number) {
    router.push({
      pathname: "/receipt/[id]/edit",
      query: { id }
    });
  }

  return (
    <ReceiptList
      create={create}
      view={view}
    />
  );
}
