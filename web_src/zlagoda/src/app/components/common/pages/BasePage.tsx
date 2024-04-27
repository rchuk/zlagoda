import {PropsWithChildren} from "react";
import { Box } from "@mui/material";

type BasePageProps = {

};

export default function BasePage(props: PropsWithChildren<BasePageProps>) {
  return (
    <Box sx={{ display: "flex", justifyContent: "center", padding: 4 }}>
      {props.children}
    </Box>
  );
}
