import {PropsWithChildren, useEffect} from "react";
import {useRouter} from "next/router";
import BasePage from "@/app/components/common/pages/BasePage";

type BaseStringIdPageProps = {
  id: string | null,
  setId: (value: string | null) => void
};

export default function BaseStringIdPage(props: PropsWithChildren<BaseStringIdPageProps>) {
  const router = useRouter();

  useEffect(() => {
    const id = String(router.query.id);
    if (router.isReady)
      props.setId(id);
  }, [router, router.query.id]);

  return (
    <BasePage>
      {props.id != null && props.children}
    </BasePage>
  );
}
