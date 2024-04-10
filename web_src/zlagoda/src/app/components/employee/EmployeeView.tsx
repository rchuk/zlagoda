import {Employee, EmployeeApi} from "../../../../generated";
import React, {useContext, useEffect, useState} from "react";
import {AlertContext} from "@/app/services/AlertService";
import {Box} from "@mui/material";
import {EmployeeRole_i18} from "@/app/i18/EmployeeRole_i18";
import dayjs from "dayjs";


type EmployeeViewProps = {
    id: number,
    employeeService: EmployeeApi
};

export default function EmployeeView(props: EmployeeViewProps): React.ReactNode {
    const [employee, setEmployee] = useState<Employee | null>();
    const showAlert = useContext(AlertContext);

    useEffect(() => {
        const fetch = async() => {
            const newEmployee = await props.employeeService.getEmployeeById({ id: props.id });
            setEmployee(newEmployee);
        };

        fetch().catch(e => showAlert(e.toString(), "error"));
    }, [props.id]);

    return (
        <Box display="flex" flexDirection="column" rowGap={1}>
            <div>
                <b>Прізвище: </b><span>{employee?.firstName}</span>
            </div>
            <div>
                <b>Ім'я: </b><span>{employee?.lastName}</span>
            </div>
            <div>
                <b>По-батькові: </b><span>{employee?.patronymic}</span>
            </div>
            <div>
                <b>Посада: </b><span>{employee ? EmployeeRole_i18[employee.role] : ""}</span>
            </div>
            <div>
                <b>Дата початку роботи: </b><span>{employee ? dayjs(employee.workStartDate).format("DD.MM.YYYY") : ""}</span>
            </div>
            <div>
                <b>Дата народження: </b><span>{employee ? dayjs(employee.birthDate).format("DD.MM.YYYY") : ""}</span>
            </div>
            <div>
                <b>Номер телефону: </b><span>{employee?.phoneNumber}</span>
            </div>
            <div>
                <b>Місто: </b><span>{employee?.city}</span>
            </div>
            <div>
                <b>Вулиця: </b><span>{employee?.street}</span>
            </div>
            <div>
                <b>Поштовий індекс: </b><span>{employee?.zipCode}</span>
            </div>
            <div>
                <b>Зарплатня: </b><span>{employee?.salary}</span>
            </div>
        </Box>
    );
}
