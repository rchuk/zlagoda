import Header from "@/app/layout/Header";
import {PropsWithChildren, useState} from "react";
import {Box, styled} from "@mui/material";
import Sidebar from "@/app/layout/Sidebar";
import BreadcrumbsComponent, {BreadcrumbServiceHandle} from "@/app/components/common/BreadcrumbsComponent";
import BreadcrumbsServiceProvider from "@/app/services/BreadcrumbsService";
import {SIDEBAR_WIDTH} from "@/app/components/common/utils/Constants";
import { Navigation } from "./Navigation";


const Main = styled('main', {
  shouldForwardProp: (prop) => prop !== 'isSidebarOpen'
})<{ isSidebarOpen: boolean; }>(({ theme, isSidebarOpen }) => ({
  flexGrow: 1,
  transition: theme.transitions.create('margin', {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  marginLeft: 0,
  ...(isSidebarOpen && {
    transition: theme.transitions.create('margin', {
      easing: theme.transitions.easing.easeOut,
      duration: theme.transitions.duration.enteringScreen,
    }),
    marginLeft: `${SIDEBAR_WIDTH}px`,
  }),
}));

type BasicLayoutProps = {

};

export default function BasicLayout(props: PropsWithChildren<BasicLayoutProps>) {
  const [isSidebarOpen, setIsSidebarOpen] = useState<boolean>(false);
  const [breadcrumbsHandle, setBreadcrumbsHandle] = useState<BreadcrumbServiceHandle | null>(null);

  const segmentMap = {
    ...Navigation.main,
    children: {
      "employee": Navigation.employee,
      "receipt": Navigation.receipt,
      "customer-card": Navigation.customerCard,
      "product": Navigation.product,
      "product-archetype": Navigation.productArchetype,
      "product-category": Navigation.productCategory,
      "users": Navigation.users,
      "extra-query": Navigation.extraQuery
    }
  };

  return (
    <Box sx={{ display: "flex", flexDirection: "column", height: "100%" }}>
      <Header isSidebarOpen={isSidebarOpen} setIsSidebarOpen={setIsSidebarOpen} />
      <Sidebar isOpen={isSidebarOpen} setIsOpen={setIsSidebarOpen}/>
      <Main isSidebarOpen={isSidebarOpen}>
        <BreadcrumbsComponent segmentMap={segmentMap} setHandle={setBreadcrumbsHandle}/>
        <BreadcrumbsServiceProvider handle={breadcrumbsHandle!}>
          {props.children}
        </BreadcrumbsServiceProvider>
      </Main>
    </Box>
  );
}
