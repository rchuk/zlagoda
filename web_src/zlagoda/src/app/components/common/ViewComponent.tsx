import React, {PropsWithChildren, useContext, useEffect} from "react";
import {AlertContext} from "@/app/services/AlertService";
import {Box} from "@mui/material";

type ViewContainerProps = {
    id: number,
    fetch: (id: number) => Promise<void>
};

export default function ViewComponent(props: PropsWithChildren<ViewContainerProps>): React.ReactNode {
    const showAlert = useContext(AlertContext);

    useEffect(() => {
        props.fetch(props.id).catch(e => showAlert(e.toString(), "error"));
    }, [props.id]);

    return (
        <Box display="flex" flexDirection="column" rowGap={1}>
            {props.children}
        </Box>
    );
}
