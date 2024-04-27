import {
  CustomerCardApi,
  EmployeeApi,
  ProductApi,
  ProductArchetypeApi,
  ProductCategoryApi,
  ReceiptApi, UsersApi
} from "../../../generated";
import React, {createContext, PropsWithChildren} from "react";

export type Services = {
  employeeService: EmployeeApi,
  productCategoryService: ProductCategoryApi,
  productArchetypeService: ProductArchetypeApi,
  productService: ProductApi,
  receiptService: ReceiptApi,
  customerCardService: CustomerCardApi,
  usersService: UsersApi
};

export const ServicesContext = createContext<Services>(null!);

export type ServicesProviderProps = {
  services: Services
};

export default function ServicesProvider(props: PropsWithChildren<ServicesProviderProps>): React.ReactNode {
  return (
    <ServicesContext.Provider value={props.services}>
      {props.children}
    </ServicesContext.Provider>
  );
}
