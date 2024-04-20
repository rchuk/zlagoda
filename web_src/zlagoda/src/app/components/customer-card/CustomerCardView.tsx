import {CustomerCard} from "../../../../generated";
import React, {useContext, useState} from "react";
import ViewComponent from "@/app/components/common/ViewComponent";
import {ServicesContext} from "@/app/services/ServiceProvider";

type CustomerCardViewProps = {
    id: number,
    onError?: (reason: any) => void,
    edit?: (id: number) => void,
    cancel?: () => void
};

export default function CustomerCardView(props: CustomerCardViewProps): React.ReactNode {
    const { customerCardService } = useContext(ServicesContext);
    const [customerCard, setCustomerCard] = useState<CustomerCard | null>(null);

    async function fetch(id: number) {
        setCustomerCard(await customerCardService.getCustomerCardById({ id }));
    }

    return (
        <ViewComponent id={props.id} fetch={fetch} onError={props.onError} edit={props.edit} cancel={props.cancel}
                       header="Перегляд картки клієнта"
        >
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
