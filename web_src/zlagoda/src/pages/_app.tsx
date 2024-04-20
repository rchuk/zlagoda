"use client"

import type { ReactElement, ReactNode } from 'react'
import type { NextPage } from 'next'
import type { AppProps } from 'next/app'
import {AdapterDayjs} from "@mui/x-date-pickers/AdapterDayjs";
import { LocalizationProvider } from '@mui/x-date-pickers';
import {AlertProvider} from "@/app/services/AlertService";
import ServicesProvider, {Services} from "@/app/services/ServiceProvider";
import {
  CustomerCardApi,
  EmployeeApi,
  ProductApi,
  ProductArchetypeApi,
  ProductCategoryApi,
  ReceiptApi
} from "../../generated";
import { Inter } from "next/font/google";
import ConfirmationDialogProvider from "@/app/services/ConfirmationDialogService";
import BasicLayout from "@/app/layout/BasicLayout";
import "./globals.css";

export type NextPageWithLayout<P = {}, IP = P> = NextPage<P, IP> & {
  getLayout?: (page: ReactElement) => ReactNode
}

type AppPropsWithLayout = AppProps & {
  Component: NextPageWithLayout
}

const inter = Inter({ subsets: ['latin'] })

export default function MyApp({ Component, pageProps }: AppPropsWithLayout) {
  const getLayout = Component.getLayout ?? ((page) => page)

  const services: Services = {
    employeeService: new EmployeeApi(),
    productCategoryService: new ProductCategoryApi(),
    productArchetypeService: new ProductArchetypeApi(),
    productService: new ProductApi(),
    receiptService: new ReceiptApi(),
    customerCardService: new CustomerCardApi()
  };

  return (
    <main className={inter.className}>
      <LocalizationProvider
        dateAdapter={AdapterDayjs} adapterLocale="uk"
      >
        <ServicesProvider services={services}>
          <AlertProvider>
            <ConfirmationDialogProvider>
              <BasicLayout>
                {getLayout(<Component {...pageProps} />)}
              </BasicLayout>
            </ConfirmationDialogProvider>
          </AlertProvider>
        </ServicesProvider>
      </LocalizationProvider>
    </main>
  );
}
