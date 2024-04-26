import {CustomerCard} from "../../../../generated";
import React, {useCallback, useContext, useEffect, useState} from "react";
import ViewComponent from "@/app/components/common/ViewComponent";
import {ServicesContext} from "@/app/services/ServiceProvider";
import {getEntityPersonFullName} from "@/app/components/common/utils/BusinessUtils";

type CustomerCardViewProps = {
    id: string,

    edit?: (id: string) => void,
    cancel?: () => void,
    onError?: (reason: any) => void
};

export default function CustomerCardView(props: CustomerCardViewProps): React.ReactNode {
    const { customerCardService } = useContext(ServicesContext);
    const [customerCard, setCustomerCard] = useState<CustomerCard | null>(null);

    const getBreadcrumb = useCallback(
        () => {
            return {
                title: getEntityPersonFullName(customerCard)
            };
        },
        [customerCard]
    );

    async function fetch(id: string) {
        setCustomerCard(await customerCardService.getCustomerCardById({ id }));
    }

    return (
        <ViewComponent id={props.id} fetch={fetch} onError={props.onError} edit={props.edit} cancel={props.cancel}
                       header="Перегляд картки клієнта" getBreadcrumb={getBreadcrumb}
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
