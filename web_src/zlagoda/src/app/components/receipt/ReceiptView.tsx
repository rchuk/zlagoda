import {
  CustomerCard,
  Employee,
  ProductArchetype,
  Receipt
} from "../../../../generated";
import React, {useContext, useEffect, useState} from "react";
import ViewComponent from "@/app/components/common/ViewComponent";
import {AlertContext} from "@/app/services/AlertService";
import {findEntity} from "@/app/components/common/utils/ObjectUtils";
import {
  formatDateTime,
  getEntityPersonFullNameWithPatronymic
} from "@/app/components/common/utils/BusinessUtils";
import {ServicesContext} from "@/app/services/ServiceProvider";
import Link from "next/link";
import {getRequestError} from "@/app/components/common/utils/RequestUtils";

type ReceiptViewProps = {
    id: number,
    onError?: (reason: any) => void,
    edit?: (id: number) => void,
    cancel?: () => void
};

export default function ReceiptView(props: ReceiptViewProps): React.ReactNode {
    const {
      receiptService,
      productArchetypeService,
      employeeService,
      customerCardService
    } = useContext(ServicesContext);
    const [receipt, setReceipt] = useState<Receipt | null>(null);
    const [productArchetypes, setProductArchetypes] = useState<ProductArchetype[] | null>(null);
    const [employee, setEmployee] = useState<Employee | null>(null);
    const [customerCard, setCustomerCard] = useState<CustomerCard | null>(null);
    const showAlert = useContext(AlertContext);

    useEffect(() => {
        const fetch = async() => {
            const response = await productArchetypeService.getProductArchetypeList();
            setProductArchetypes(response.items);
        };

        fetch().catch(e => getRequestError(e).then(m => showAlert(m, "error")));
    }, []);

    async function fetch(id: number) {
        const newReceipt = await receiptService.getReceiptById({ id });
        setReceipt(newReceipt);
        setEmployee(await employeeService.getEmployeeById({ id: newReceipt.cashierId }));
        if (newReceipt.customerCardId != null)
            setCustomerCard(await customerCardService.getCustomerCardById({ id: newReceipt.customerCardId }));
        else
            setCustomerCard(null);
    }

    // TODO: Add links to archetype, client card and cashier
    return (
        <ViewComponent id={props.id} fetch={fetch} onError={props.onError} edit={props.edit} cancel={props.cancel}
                       header="Перегляд чеку"
        >
            <div>
                <b>Касир: </b>
                <Link href={`/employee/${employee?.id}`}>
                  {getEntityPersonFullNameWithPatronymic(employee)}
                </Link>
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
