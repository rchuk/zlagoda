import {PropsWithChildren} from "react";
import {useRouter} from "next/router";
import ProgressSpinner from "@/app/components/common/ProgressSpinner";
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
