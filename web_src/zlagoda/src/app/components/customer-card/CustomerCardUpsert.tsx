import {CustomerCardView} from "../../../../generated";
import React, {useContext, useState} from "react";
import {TextField} from "@mui/material";
import Grid from "@mui/material/Unstable_Grid2";
import UpsertComponent from "@/app/components/common/UpsertComponent";
import {ServicesContext} from "@/app/services/ServiceProvider";

function getDefaultCustomerCardView(): CustomerCardView {
    return {
        firstName: "",
        lastName: "",
        patronymic: "",
        phoneNumber: "",
        discountPercent: 0,
        city: "",
        street: "",
        zipCode: ""
    };
}

type CustomerCardUpsertProps = {
    initialId: number | null,
    cancel?: () => void,
    onError?: () => void
};

export default function CustomerCardUpsert(props: CustomerCardUpsertProps): React.ReactNode {
    const { customerCardService } = useContext(ServicesContext);
    const [view, setView] = useState<CustomerCardView>(getDefaultCustomerCardView);

    async function fetch(id: number) {
        const {id: _, ...newView} = await customerCardService.getCustomerCardById({ id });
        setView(newView);
    }

    async function update(id: number) {
        await customerCardService.updateCustomerCard({id, customerCardView: view});
    }

    async function create(): Promise<number> {
        return await customerCardService.createCustomerCard({customerCardView: view});
    }

    return (
        <UpsertComponent
            initialId={props.initialId}
            resetView={() => setView(getDefaultCustomerCardView)}
            fetch={fetch}
            create={create}
            update={update}
            cancel={props.cancel}
            onError={props.onError}
        >
            <Grid xs={6}>
                <TextField label="Прізвище"
                           required
                           fullWidth
                           value={view.firstName}
                           onChange={e => setView({...view, firstName: e.target.value})}
                />
            </Grid>
            <Grid xs={6}>
                <TextField label="Ім'я"
                           required
                           fullWidth
                           value={view.lastName}
                           onChange={e => setView({...view, lastName: e.target.value})}
                />
            </Grid>
            <Grid xs={6}>
                <TextField label="По-батькові"
                           fullWidth
                           value={view.patronymic} onChange={e => setView({...view, patronymic: e.target.value})}
                />
            </Grid>
            <Grid xs={6}>
                <TextField label="Номер телефону"
                           required
                           fullWidth
                           value={view.phoneNumber}
                           onChange={e => setView({...view, phoneNumber: e.target.value})}
                />
            </Grid>
            <Grid xs={6}>
                <TextField label="Місто"
                           fullWidth
                           value={view.city} onChange={e => setView({...view, city: e.target.value})}
                />
            </Grid>
            <Grid xs={6}>
                <TextField label="Поштовий індекс"
                           fullWidth
                           value={view.zipCode}
                           onChange={e => setView({...view, zipCode: e.target.value})}
                />
            </Grid>
            <Grid xs={12}>
                <TextField label="Вулиця"
                           fullWidth
                           value={view.street}
                           onChange={e => setView({...view, street: e.target.value})}
                />
            </Grid>
            <Grid xs={6}>
                <TextField label="Відсоток знижки"
                           type="number"
                           required
                           inputProps={{min: 0, max: 100}}
                           fullWidth
                           value={view.discountPercent}
                           onChange={e => setView({...view, discountPercent: Number(e.target.value)})}
                />
            </Grid>
        </UpsertComponent>
    );
}
