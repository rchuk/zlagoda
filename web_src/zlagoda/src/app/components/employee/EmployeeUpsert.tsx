import React, {useContext, useState} from "react";
import {FormControl, InputLabel, MenuItem, Select, TextField} from "@mui/material";
import {DatePicker} from "@mui/x-date-pickers";
import {EmployeeRole, EmployeeView} from "../../../../generated";
import dayjs from "dayjs";
import Grid from "@mui/material/Unstable_Grid2";
import {EmployeeRole_i18} from "@/app/i18/EmployeeRole_i18";
import UpsertComponent from "@/app/components/common/UpsertComponent";
import {ServicesContext} from "@/app/services/ServiceProvider";

type EmployeeUpsertProps = {
    initialId?: number
};

function getDefaultEmployeeView(): EmployeeView {
    return {
        firstName: "",
        lastName: "",
        patronymic: "",
        role: EmployeeRole.Cashier,
        salary: 0,
        workStartDate: dayjs().toDate(),
        birthDate: dayjs().toDate(),
        phoneNumber: "",
        city: "",
        street: "",
        zipCode: ""
    };
}

export default function EmployeeUpsert(props: EmployeeUpsertProps): React.ReactNode {
    const { employeeService } = useContext(ServicesContext);
    const [view, setView] = useState<EmployeeView>(getDefaultEmployeeView);

    async function fetch(id: number) {
        const {id: _, ...newView} = await employeeService.getEmployeeById({ id });
        setView(newView);
    }

    async function update(id: number) {
        await employeeService.updateEmployee({id, employeeView: view});
    }

    async function create(): Promise<number> {
        return await employeeService.createEmployee({employeeView: view});
    }

    function cancel() {

    }

    return (
        <UpsertComponent
            initialId={props.initialId}
            resetView={() => setView(getDefaultEmployeeView)}
            fetch={fetch}
            create={create}
            update={update}
            cancel={cancel}>
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
                <FormControl fullWidth>
                    <InputLabel>Посада</InputLabel>
                    <Select
                        label="Посада"
                        required
                        value={view.role}
                        onChange={e => setView({...view, role: e.target.value as EmployeeRole})}
                    >
                        {Object.values(EmployeeRole).map(value => (
                            <MenuItem key={value} value={value}>{EmployeeRole_i18[value]}</MenuItem>
                        ))}
                    </Select>
                </FormControl>
            </Grid>

            <Grid xs={6}>
                <DatePicker label="Дата початку роботи"
                            disableFuture
                            slotProps={{ textField: { fullWidth: true } }}
                            value={dayjs(view.workStartDate)}
                            onChange={value => setView({...view, workStartDate: (value ?? dayjs())?.toDate()})}
                />
            </Grid>
            <Grid xs={6}>
                <DatePicker label="Дата народження"
                            disableFuture
                            slotProps={{ textField: { fullWidth: true } }}
                            value={dayjs(view.birthDate)}
                            onChange={value => setView({...view, birthDate: (value ?? dayjs())?.toDate()})}
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
                           required
                           fullWidth
                           value={view.city} onChange={e => setView({...view, city: e.target.value})}
                />
            </Grid>
            <Grid xs={6}>
                <TextField label="Вулиця"
                           required
                           fullWidth
                           value={view.street}
                           onChange={e => setView({...view, street: e.target.value})}
                />
            </Grid>
            <Grid xs={6}>
                <TextField label="Поштовий індекс"
                           required
                           fullWidth
                           value={view.zipCode}
                           onChange={e => setView({...view, zipCode: e.target.value})}
                />
            </Grid>
            <Grid xs={6}>
                <TextField label="Зарплатня"
                           type="number"
                           required
                           inputProps={{min: 0}}
                           fullWidth
                           value={view.salary}
                           onChange={e => setView({...view, salary: Number(e.target.value)})}
                />
            </Grid>
        </UpsertComponent>
    );
}
