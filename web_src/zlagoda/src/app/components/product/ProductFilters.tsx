import {FormControl, Grid, InputLabel, MenuItem, Select} from "@mui/material";
import ListFiltersComponent from "@/app/components/common/ListFiltersComponent";
import {ProductCriteria} from "../../../../generated";
import React from "react";

type ReceiptFiltersProps = {
  criteria: ProductCriteria,
  setCriteria: (value: ProductCriteria) => void
};

export default function ProductFilters(props: ReceiptFiltersProps) {
  function setHasDiscount(value: string) {
    props.setCriteria({...props.criteria, hasDiscount: value !== "" ? (value === "true") : undefined});
  }

  return (
    <ListFiltersComponent>
      <Grid item xs={3}>
        <FormControl fullWidth>
          <InputLabel>Знижка</InputLabel>
          <Select
            label="Знижка"
            required
            value={props.criteria.hasDiscount !== undefined ? String(props.criteria.hasDiscount) : ""}
            onChange={e => setHasDiscount(e.target.value)}
          >
            <MenuItem key={"null"} value={""}>Усі</MenuItem>
            <MenuItem key={"true"} value={"true"}>Так</MenuItem>
            <MenuItem key={"false"} value={"false"}>Ні</MenuItem>
          </Select>
        </FormControl>
      </Grid>
    </ListFiltersComponent>
  );
}

