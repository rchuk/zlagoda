import {CustomerCardApi, CustomerCard} from "../../../../generated";
import React, {useState} from "react";
import ViewComponent from "@/app/components/common/ViewComponent";

type CustomerCardViewProps = {
    id: number,
    customerCardService: CustomerCardApi
};

export default function CustomerCardView(props: CustomerCardViewProps): React.ReactNode {
    const [customerCard, setCustomerCard] = useState<CustomerCard | null>(null);

    async function fetch(id: number) {
        setCustomerCard(await props.customerCardService.getCustomerCardById({ id }));
    }

    return (
        <ViewComponent id={props.id} fetch={fetch}>
            <div>
                <b>Прізвище: </b><span>{customerCard?.firstName}</span>
            </div>
            <div>
                <b>Ім'я: </b><span>{customerCard?.lastName}</span>
            </div>
            <div>
                <b>По-батькові: </b><span>{customerCard?.patronymic}</span>
            </div>
            <div>
                <b>Відсоток знижки: </b><span>{customerCard?.discountPercent}</span>
            </div>
            <div>
                <b>Номер телефону: </b><span>{customerCard?.phoneNumber}</span>
            </div>
            <div>
                <b>Місто: </b><span>{customerCard?.city}</span>
            </div>
            <div>
                <b>Вулиця: </b><span>{customerCard?.street}</span>
            </div>
            <div>
                <b>Поштовий індекс: </b><span>{customerCard?.zipCode}</span>
            </div>
        </ViewComponent>
    );
}
