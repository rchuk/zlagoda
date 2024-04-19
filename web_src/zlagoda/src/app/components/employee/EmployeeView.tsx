import {Employee, EmployeeApi} from "../../../../generated";
import React, {useState} from "react";
import {EmployeeRole_i18} from "@/app/i18/EmployeeRole_i18";
import dayjs from "dayjs";
import ViewComponent from "@/app/components/common/ViewComponent";
import {formatDate} from "@/app/components/common/utils/BusinessUtils";


type EmployeeViewProps = {
    id: number,
    employeeService: EmployeeApi
};

export default function EmployeeView(props: EmployeeViewProps): React.ReactNode {
    const [employee, setEmployee] = useState<Employee | null>(null);

    async function fetch(id: number) {
        setEmployee(await props.employeeService.getEmployeeById({ id }));
    }

    return (
        <ViewComponent id={props.id} fetch={fetch}>
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
                <b>Дата початку роботи: </b><span>{formatDate(employee?.workStartDate ?? null)}</span>
            </div>
            <div>
                <b>Дата народження: </b><span>{formatDate(employee?.birthDate ?? null)}</span>
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
        </ViewComponent>
    );
}
