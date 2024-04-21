import React, {PropsWithChildren, useContext, useEffect, useState} from "react";
import {AlertContext} from "@/app/services/AlertService";
import {Box, Button} from "@mui/material";
import ProgressSpinner from "@/app/components/common/ProgressSpinner";
import {getRequestError} from "@/app/components/common/utils/RequestUtils";

type ViewComponentProps = {
    id: number,
    header: string,
    fetch: (id: number) => Promise<void>,
    edit?: (id: number) => void,
    onError?: (reason: any) => void,
    cancel?: () => void
};

export default function ViewComponent(props: PropsWithChildren<ViewComponentProps>): React.ReactNode {
    const [isReady, setIsReady] = useState<boolean>(false);
    const showAlert = useContext(AlertContext);

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
             sx={{ width: 500, margin: 2 }}>
            <h2 style={{ textAlign: "center" }}>{props.header}</h2>
            {props.children}
            <Box display="flex" justifyContent="flex-end" columnGap={1}>
                {props.edit &&
                    <Button variant="outlined" onClick={_ => props.edit!(props.id)}>
                        Редагувати
                    </Button>
                }
                <Button variant="outlined" onClick={props.cancel}>Відміна</Button>
            </Box>
        </Box>
    );
}
