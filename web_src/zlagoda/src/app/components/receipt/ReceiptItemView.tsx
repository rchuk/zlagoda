import {ReceiptItem} from "../../../../generated";
import {Box, Chip, ListItem} from "@mui/material";
import {useRouter} from "next/router";


type ReceiptItemsProps = {
  item: ReceiptItem,
  name: string
};

export function ReceiptItemView(props: ReceiptItemsProps) {
  const router = useRouter();

  const total = props.item.quantity * props.item.price;

  function productRedirect() {
    router.push({
      pathname: "/product-archetype/[id]",
      query: { id: props.item.productArchetype }
    });
  }

  return (
    <ListItem>
      <Box display="flex" justifyContent="space-between" width="100%">
        <Chip variant="outlined" label={props.name} sx={{ flex: 1 }} onClick={productRedirect} />
        <Box flex={1} alignContent="center" padding={1}>
          <span>{props.item.quantity} X {props.item.price} = {total}</span>
        </Box>
      </Box>
    </ListItem>
  );
}
