import React, {useContext, useEffect, useState} from "react";
import {Box, Button, MenuItem, Select, TextField} from "@mui/material";
import {DatePicker} from "@mui/x-date-pickers";
import {EmployeeApi, EmployeeRole, EmployeeView} from "../../../../generated";
import dayjs from "dayjs";
import Grid from "@mui/material/Unstable_Grid2";
import {EmployeeRole_i18} from "@/app/i18/EmployeeRole_i18";
import {AlertContext} from "@/app/services/AlertService";

type EmployeeUpsertProps = {
    initialId?: number,
    employeeService: EmployeeApi
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
    const [id, setId] = useState<number | null>(null);
    const [view, setView] = useState<EmployeeView>(getDefaultEmployeeView());
    const showAlert = useContext(AlertContext);

    useEffect(() => {
        if (props.initialId == null) {
            setView(getDefaultEmployeeView());
            return;
        }

        setId(props.initialId);
        const fetch = async() => {
            const {id, ...newView} = await props.employeeService.getEmployeeById({ id: props.initialId! });
            setView(newView);
        };

        fetch().catch(e => showAlert(e.toString(), "error"));
    }, [props.initialId])

    function update() {
        const update = async() => {
            await props.employeeService.updateEmployee({id: id!, employeeView: view});
        };

        update()
            .then(console.log)
            .catch(e => showAlert(e.toString(), "error"));
    }

    function create() {
        const create = async() => {
            const id = await props.employeeService.createEmployee({employeeView: view});
            setId(id);
        };

        create().catch(e => showAlert(e.toString(), "error"));
    }

    function submit() {
        if (id == null)
            create()
        else
            update();
    }

    function cancel() {

    }

    return (
        <Box style={{width: 500}} component="form" onSubmit={e => {e.preventDefault(); submit()}}>
            <Grid container columnSpacing={1} rowSpacing={2}>
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
                    <Select
                        label="Посада"
                        required
                        fullWidth
                        value={view.role}
                        onChange={e => setView({...view, role: e.target.value as EmployeeRole})}
                    >
                        {Object.values(EmployeeRole).map(value => (
                            <MenuItem key={value} value={value}>{EmployeeRole_i18[value]}</MenuItem>
                        ))}
                    </Select>
                </Grid>

                <Grid xs={6}>
                    <DatePicker label="Дата початку роботи"
                                disableFuture
                                value={dayjs(view.workStartDate)}
                                onChange={value => setView({...view, workStartDate: (value ?? dayjs())?.toDate()})}
                    />
                </Grid>
                <Grid xs={6}>
                    <DatePicker label="Дата народження"
                                disableFuture
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

                <Grid xs={12}>
                    <Box display="flex" justifyContent="flex-end" columnGap={1}>
                        <Button type="submit" variant="outlined">Зберегти</Button>
                        <Button variant="outlined" onClick={cancel}>Відміна</Button>
                    </Box>
                </Grid>
            </Grid>
        </Box>
    );
}
