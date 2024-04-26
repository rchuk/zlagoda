import { Grid } from "@mui/material";
import {PropsWithChildren} from "react";


type ListFiltersComponentProps = {

};

export default function ListFiltersComponent(props: PropsWithChildren<ListFiltersComponentProps>) {
  return (
    <Grid container width="100%" gap={2}>
      {props.children}
    </Grid>
  );
}
