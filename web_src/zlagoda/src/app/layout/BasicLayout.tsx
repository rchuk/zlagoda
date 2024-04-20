import Header from "@/app/layout/Header";
import Footer from "@/app/layout/Footer";
import {PropsWithChildren} from "react";
import {Box} from "@mui/material";

type BasicLayoutProps = {

};

export default function BasicLayout(props: PropsWithChildren<BasicLayoutProps>) {
  return (
    <Box sx={{ display: "flex", flexDirection: "column", height: "100%" }}>
      <Header />
      <Box sx={{ flex: "1" }}>
        {props.children}
      </Box>
      <Footer />
    </Box>
  );
}
