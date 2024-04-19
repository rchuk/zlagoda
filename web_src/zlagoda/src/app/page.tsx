"use client"

import EmployeeUpsert from "@/app/components/employee/EmployeeUpsert";
import {LocalizationProvider} from "@mui/x-date-pickers";
import {AdapterDayjs} from "@mui/x-date-pickers/AdapterDayjs";
import {AlertProvider} from "@/app/services/AlertService";
import EmployeeView from "@/app/components/employee/EmployeeView";
import ProductCategoryUpsert from "@/app/components/product-category/ProductCategoryUpsert";
import ProductArchetypeUpsert from "@/app/components/product-archetype/ProductArchetypeUpsert";
import ProductArchetypeView from "@/app/components/product-archetype/ProductArchetypeView";
import CustomerCardUpsert from "@/app/components/customer-card/CustomerCardUpsert";
import CustomerCardView from "@/app/components/customer-card/CustomerCardView";
import ProductUpsert from "@/app/components/product/ProductUpsert";
import ProductView from "@/app/components/product/ProductView";
import ReceiptView from "@/app/components/receipt/ReceiptView";
import EmployeeList from "@/app/components/employee/EmployeeList"
import ProductCategoryList from "@/app/components/product-category/ProductCategoryList";
import ProductList from "@/app/components/product/ProductList";
import ProductArchetypeList from "@/app/components/product-archetype/ProductArchetypeList";
import CustomerCardList from "@/app/components/customer-card/CustomerCardList";
import ReceiptList from "@/app/components/receipt/ReceiptList";
import ServicesProvider, {Services} from "@/app/services/ServiceProvider";
import {
  CustomerCardApi,
  EmployeeApi,
  ProductApi,
  ProductArchetypeApi,
  ProductCategoryApi,
  ReceiptApi
} from "../../generated";

export default function Home() {
  const services: Services = {
    employeeService: new EmployeeApi(),
    productCategoryService: new ProductCategoryApi(),
    productArchetypeService: new ProductArchetypeApi(),
    productService: new ProductApi(),
    receiptService: new ReceiptApi(),
    customerCardService: new CustomerCardApi()
  };

  return (
    <div>
      <LocalizationProvider
        dateAdapter={AdapterDayjs} adapterLocale="uk"
      >
        <AlertProvider>
          <ServicesProvider services={services}>
            <h1>Hello world!</h1>
            <EmployeeUpsert></EmployeeUpsert>
            <EmployeeView></EmployeeView>
            <ProductCategoryUpsert></ProductCategoryUpsert>
            <ProductArchetypeUpsert></ProductArchetypeUpsert>
            <ProductArchetypeView></ProductArchetypeView>
            <CustomerCardUpsert></CustomerCardUpsert>
            <CustomerCardView></CustomerCardView>
            <ProductUpsert></ProductUpsert>
            <ProductView></ProductView>
            <ReceiptView></ReceiptView>
            <EmployeeList></EmployeeList>
            <ProductCategoryList></ProductCategoryList>
            <ProductList></ProductList>
            <ProductArchetypeList></ProductArchetypeList>
            <CustomerCardList></CustomerCardList>
            <ReceiptList></ReceiptList>
          </ServicesProvider>
        </AlertProvider>
      </LocalizationProvider>
    </div>
  );
}
