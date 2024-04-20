import {useRouter} from "next/router";
import ReceiptList from "@/app/components/receipt/ReceiptList";
import {Box} from "@mui/material";

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
    <Box>
      <ReceiptList
        create={create}
        view={view}
      />
    </Box>
  );
}
