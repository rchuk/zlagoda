"use client"

import type { ReactElement, ReactNode } from 'react'
import type { NextPage } from 'next'
import type { AppProps } from 'next/app'
import {AdapterDayjs} from "@mui/x-date-pickers/AdapterDayjs";
import { LocalizationProvider } from '@mui/x-date-pickers';
import {AlertProvider} from "@/app/services/AlertService";
import ServicesProvider, {Services} from "@/app/services/ServiceProvider";
import {
  Configuration,
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
import {useEffect, useState} from "react";
import AuthServiceProvider from "@/app/services/AuthService";
import {useRouter} from "next/router";

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
});

function getDefaultServices(): Services {
  return {
    employeeService: new EmployeeApi(),
    productCategoryService: new ProductCategoryApi(),
    productArchetypeService: new ProductArchetypeApi(),
    productService: new ProductApi(),
    receiptService: new ReceiptApi(),
    customerCardService: new CustomerCardApi()
  };
}

function tryGetAuthToken(): string | null {
  const token = localStorage.getItem("access-token");
  if (token != null && token.length !=0)
    return token;

  return null;
}

export default function MyApp({ Component, pageProps }: AppPropsWithLayout) {
  const getLayout = Component.getLayout ?? ((page) => page);

  const [services, setServices] = useState<Services>(getDefaultServices);
  const [authToken, setAuthToken] = useState<string | null>(null);
  const router = useRouter();

  useEffect(() => {
    setAuthToken(tryGetAuthToken);
  }, []);

  useEffect(() => {
    if (authToken == null)
      router.push("/login");
  }, [router.asPath]);

  useEffect(() => {
    if (authToken == null) {
      setServices(getDefaultServices);
      return;
    }

    let config = new Configuration({
      headers: {
        "Authorization": "Bearer " + authToken
      }
    });

    setServices({
      employeeService: new EmployeeApi(config),
      productCategoryService: new ProductCategoryApi(config),
      productArchetypeService: new ProductArchetypeApi(config),
      productService: new ProductApi(config),
      receiptService: new ReceiptApi(config),
      customerCardService: new CustomerCardApi(config)
    });
  }, [authToken]);

  return (
    <main className={roboto.className}>
      <LocalizationProvider
        dateAdapter={AdapterDayjs} adapterLocale="uk"
      >
        <AuthServiceProvider token={authToken} setToken={setAuthToken}>
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
        </AuthServiceProvider>
      </LocalizationProvider>
    </main>
  );
}
