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

export default function Home() {
  return (
    <div>
        <LocalizationProvider
            dateAdapter={AdapterDayjs} adapterLocale="uk"
        >
            <AlertProvider>
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
            </AlertProvider>
        </LocalizationProvider>
    </div>
  );
}
