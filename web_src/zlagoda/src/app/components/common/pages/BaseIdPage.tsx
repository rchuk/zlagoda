import {PropsWithChildren, useContext, useEffect} from "react";
import {useRouter} from "next/router";
import BasePage from "@/app/components/common/pages/BasePage";
import {AlertContext} from "@/app/services/AlertService";

type BaseIdPageProps = {
  id: number | null,
  setId: (value: number | null) => void
};

export default function BaseIdPage(props: PropsWithChildren<BaseIdPageProps>) {
  const router = useRouter();
  const showAlert = useContext(AlertContext);

  useEffect(() => {
    const id = Number(router.query.id);
    if (router.isReady) {
      if (Number.isNaN(id)) {
        showAlert("Невірний URL", "error");

        router.back();
      } else {
        props.setId(id);
      }
    }
  }, [router, router.query.id]);

  return (
    <BasePage>
      {props.id != null && props.children}
    </BasePage>
  );
}
