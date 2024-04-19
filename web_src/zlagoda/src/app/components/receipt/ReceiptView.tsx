import {
  CustomerCard,
  CustomerCardApi, Employee,
  EmployeeApi, ProductArchetype,
  ProductArchetypeApi,
  Receipt,
  ReceiptApi
} from "../../../../generated";
import React, {useContext, useEffect, useState} from "react";
import ViewComponent from "@/app/components/common/ViewComponent";
import dayjs from "dayjs";
import {AlertContext} from "@/app/services/AlertService";
import {findEntity} from "@/app/components/common/utils/ObjectUtils";
import {
  formatDateTime,
  getEntityPersonFullName,
  getEntityPersonFullNameWithPatronymic
} from "@/app/components/common/utils/BusinessUtils";

type ReceiptViewProps = {
    id: number,
    receiptService: ReceiptApi,
    productArchetypeService: ProductArchetypeApi,
    employeeService: EmployeeApi,
    customerCardService: CustomerCardApi
};

export default function ReceiptView(props: ReceiptViewProps): React.ReactNode {
    const [receipt, setReceipt] = useState<Receipt | null>(null);
    const [productArchetypes, setProductArchetypes] = useState<ProductArchetype[] | null>(null);
    const [employee, setEmployee] = useState<Employee | null>(null);
    const [customerCard, setCustomerCard] = useState<CustomerCard | null>(null);
    const showAlert = useContext(AlertContext);

    useEffect(() => {
        const fetch = async() => {
            const response = await props.productArchetypeService.getProductArchetypeList();
            setProductArchetypes(response.items);
        };

        fetch().catch(e => showAlert(e.toString(), "error"));
    });

    async function fetch(id: number) {
        setReceipt(await props.receiptService.getReceiptById({ id }));
        // TODO: Test
        setEmployee(await props.employeeService.getEmployeeById({ id: receipt!.cashierId }));
        if (receipt?.customerCardId != null)
            setCustomerCard(await props.customerCardService.getCustomerCardById({ id: receipt!.customerCardId }));
        else
            setCustomerCard(null);
    }

    // TODO: Add links to archetype, client card and cashier
    return (
        <ViewComponent id={props.id} fetch={fetch}>
            <div>
                <b>Касир: </b><span>{getEntityPersonFullNameWithPatronymic(employee)}</span>
            </div>
            <div>
                <b>Картка клієнта: </b><span>{getEntityPersonFullNameWithPatronymic(customerCard)}</span>
            </div>
            <div>
                <b>Дата створення: </b><span>{formatDateTime(receipt?.dateTime ?? null)}</span>
            </div>
            <div>
                <b>ПДВ: </b><span>{receipt?.vat}</span>
            </div>
            <div>
                <b>Вартість: </b><span>{receipt?.totalPrice}</span>
            </div>
            <div>
                <b>Товари: </b>
                <ul>
                    {receipt?.items.map(item =>
                        <li>
                            {findEntity(productArchetypes, item.productArchetype)?.name ?? ""} | Ціна: {item.price} | Кількість: {item.quantity}
                        </li>
                    )}
                </ul>
            </div>
        </ViewComponent>
    );
}
