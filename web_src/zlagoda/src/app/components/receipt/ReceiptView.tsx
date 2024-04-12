import {
    CustomerCard,
    CustomerCardApi, Employee,
    EmployeeApi,
    ProductArchetypeApi,
    Receipt,
    ReceiptApi
} from "../../../../generated";
import React, {useContext, useEffect, useState} from "react";
import ViewComponent from "@/app/components/common/ViewComponent";
import dayjs from "dayjs";
import {AlertContext} from "@/app/services/AlertService";

type ProductArchetypeShort = {
    id: number,
    name: string
};

type ReceiptViewProps = {
    id: number,
    receiptService: ReceiptApi,
    productArchetypeService: ProductArchetypeApi,
    employeeService: EmployeeApi,
    customerCardService: CustomerCardApi
};

export default function ReceiptView(props: ReceiptViewProps): React.ReactNode {
    const [receipt, setReceipt] = useState<Receipt | null>(null);
    const [productArchetypes, setProductArchetypes] = useState<Array<ProductArchetypeShort> | null>(null);
    const [employee, setEmployee] = useState<Employee | null>(null);
    const [customerCard, setCustomerCard] = useState<CustomerCard | null>(null);
    const showAlert = useContext(AlertContext);

    useEffect(() => {
        const fetch = async() => {
            const newProductArchetypes = await props.productArchetypeService.getProductArchetypeList();
            setProductArchetypes(newProductArchetypes.map(archetype => ({
                id: archetype.id,
                name: archetype.name
            })));
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
                <b>Касир: </b><span>{employee ? `${employee?.firstName} ${employee?.lastName}` : ""}</span>
            </div>
            <div>
                <b>Картка клієнта: </b><span>{customerCard ? `${customerCard?.firstName} ${customerCard?.lastName}` : ""}</span>
            </div>
            <div>
                <b>Дата створення: </b><span>{receipt ? dayjs(receipt!.dateTime).format("DD.MM.YYYY") : ""}</span>
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
                            {productArchetypes![item.productArchetype].name} | Ціна: {item.price} | Кількість: {item.quantity}
                        </li>
                    )}
                </ul>
            </div>
        </ViewComponent>
    );
}
