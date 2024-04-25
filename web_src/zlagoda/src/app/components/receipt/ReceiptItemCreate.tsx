import {Box, Chip, TextField} from "@mui/material";
import React from "react";
import {ReceiptItemView, ReceiptView} from "../../../../generated";


type ReceiptItemProps = {
  view: ReceiptView,
  setView: (value: ReceiptView) => void,
  product: string,
  productName: string,
};

export default function ReceiptItemCreate(props: ReceiptItemProps) {
  function getItem(): ReceiptItemView {
    return props.view.items.find(item => item.product == props.product)!;
  }

  function setItem(newItem: ReceiptItemView) {
    const newItems = props.view.items.map(item => {
      if (item.product == props.product) {
        return newItem;
      } else {
        return item;
      }
    });

    props.setView({...props.view, items: newItems});
  }

  return (
    <Box display="flex" padding={2} alignItems="center" justifyContent="space-between" columnGap={1}>
      <Chip variant="outlined" label={props.productName} sx={{ flex: 1 }} />
      <TextField label="Кількість"
                 type="number"
                 required
                 inputProps={{min: 1}}
                 fullWidth
                 value={getItem().quantity}
                 onChange={e => setItem({...getItem(), quantity: Number(e.target.value)})}
                 sx={{ flex: 1 }}
      />
    </Box>
  );
}
