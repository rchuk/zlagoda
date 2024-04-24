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
import ConfirmationDialogProvider from "@/app/services/ConfirmationDialogService";
import BasicLayout from "@/app/layout/BasicLayout";
import FullscreenServiceProvider from "@/app/services/FullscreenService";
import { Roboto } from 'next/font/google'
import { createTheme } from '@mui/material/styles';
import {ThemeProvider} from "@mui/system";
import "./globals.css";

export type NextPageWithLayout<P = {}, IP = P> = NextPage<P, IP> & {
  getLayout?: (page: ReactElement) => ReactNode
}

type AppPropsWithLayout = AppProps & {
  Component: NextPageWithLayout
}

const roboto = Roboto({
  weight: "400",
  subsets: ["latin", "cyrillic"]
})

declare module '@mui/material/styles' {
  interface Palette {
    almostWhite: Palette["primary"];
  }

  interface PaletteOptions {
    almostWhite?: PaletteOptions["primary"];
  }
}

const theme = createTheme({
  palette: {
    primary: {
      main: "#8a0709"
    },
    secondary: {
      main: "#078a88"
    },
    almostWhite: {
      main: "#eeeeee"
    }
  }
})

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
    <main className={roboto.className}>
      <LocalizationProvider
        dateAdapter={AdapterDayjs} adapterLocale="uk"
      >
        <ServicesProvider services={services}>
          <AlertProvider>
            <ConfirmationDialogProvider>
              <FullscreenServiceProvider>
                <ThemeProvider theme={theme}>
                  <BasicLayout>
                    {getLayout(<Component {...pageProps} />)}
                  </BasicLayout>
                </ThemeProvider>
              </FullscreenServiceProvider>
            </ConfirmationDialogProvider>
          </AlertProvider>
        </ServicesProvider>
      </LocalizationProvider>
    </main>
  );
}
