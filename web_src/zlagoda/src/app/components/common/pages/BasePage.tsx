import {PropsWithChildren} from "react";
import {useRouter} from "next/router";
import ProgressSpinner from "@/app/components/common/ProgressSpinner";

type BasePageProps = {

};

export default function BasePage(props: PropsWithChildren<BasePageProps>) {
  const router = useRouter();

  return !router.isReady
    ? (<ProgressSpinner />)
    : props.children;
}
