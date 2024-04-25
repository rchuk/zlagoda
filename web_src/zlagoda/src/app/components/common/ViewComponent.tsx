import React, {PropsWithChildren, useContext, useEffect, useState} from "react";
import {AlertContext} from "@/app/services/AlertService";
import {Box, Button, Typography} from "@mui/material";
import ProgressSpinner from "@/app/components/common/ProgressSpinner";
import {getRequestError} from "@/app/components/common/utils/RequestUtils";
import {EntityId} from "@/app/components/common/utils/ObjectUtils";
import {BreadcrumbItem} from "@/app/components/common/BreadcrumbsComponent";
import {BreadcrumbsServiceContext} from "@/app/services/BreadcrumbsService";

type ViewComponentProps<IdT extends EntityId> = {
    id: IdT,
    header: string,
    fetch: (id: IdT) => Promise<void>,

    edit?: (id: IdT) => void,
    cancel?: () => void,
    onError?: (reason: any) => void,

    getBreadcrumb?: () => BreadcrumbItem
};

export default function ViewComponent<IdT extends EntityId>(props: PropsWithChildren<ViewComponentProps<IdT>>): React.ReactNode {
    const [isReady, setIsReady] = useState<boolean>(false);
    const showAlert = useContext(AlertContext);
    const breadcrumbsHandle = useContext(BreadcrumbsServiceContext);

  useEffect(() => {
    if (isReady) {
      if (props.getBreadcrumb !== undefined)
        breadcrumbsHandle.modify(props.getBreadcrumb());
    }
  }, [isReady]);

    useEffect(() => {
        props.fetch(props.id)
          .then(_ => setIsReady(true))
          .catch(e => {
              getRequestError(e).then(m => showAlert(m, "error"))

              props.onError?.(e);
          });
    }, [props.id]);

    if (!isReady)
        return <ProgressSpinner />;

    return (
        <Box display="flex" flexDirection="column" rowGap={1}
             sx={{ width: 500 }}>
            <Typography variant="h4" sx={{ marginBottom: 4 }}>
              {props.header}
            </Typography>
            {props.children}
            <Box display="flex" justifyContent="flex-end" columnGap={1}>
                {props.edit &&
                    <Button variant="outlined" onClick={_ => props.edit!(props.id)}>
                        Редагувати
                    </Button>
                }
                <Button variant="outlined" onClick={props.cancel}>Назад</Button>
            </Box>
        </Box>
    );
}
