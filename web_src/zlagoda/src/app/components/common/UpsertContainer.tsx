import React, {PropsWithChildren} from "react";
import {Box, Button} from "@mui/material";
import Grid from "@mui/material/Unstable_Grid2";


type UpsertContainerProps = {
    submit: () => void;
    cancel: () => void;
};

export default function UpsertContainer(props: PropsWithChildren<UpsertContainerProps>): React.ReactNode {
    return (
        <Box component="form" onSubmit={e => {e.preventDefault(); props.submit()}}>
            <Grid container columnSpacing={1} rowSpacing={2}>
                {props.children}

                <Grid xs={12}>
                    <Box display="flex" justifyContent="flex-end" columnGap={1}>
                        <Button type="submit" variant="outlined">Зберегти</Button>
                        <Button variant="outlined" onClick={props.cancel}>Відміна</Button>
                    </Box>
                </Grid>
            </Grid>
        </Box>
    )
}