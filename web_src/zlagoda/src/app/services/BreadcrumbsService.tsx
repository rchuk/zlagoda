import {BreadcrumbServiceHandle} from "@/app/components/common/BreadcrumbsComponent";
import {createContext, PropsWithChildren} from "react";

type BreadcrumbsServiceProviderProps = {
  handle: BreadcrumbServiceHandle
};

export const BreadcrumbsServiceContext = createContext<BreadcrumbServiceHandle>(null!);

export default function BreadcrumbsServiceProvider(props: PropsWithChildren<BreadcrumbsServiceProviderProps>) {
  return (
    <BreadcrumbsServiceContext.Provider value={props.handle}>
      {props.children}
    </BreadcrumbsServiceContext.Provider>
  );
}
