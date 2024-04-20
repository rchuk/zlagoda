import {
  CustomerCard,
  Employee,
  Receipt,
  ReceiptCriteria,
  ReceiptListResponse
} from "../../../../generated";
import React, {useContext, useEffect, useState} from "react";
import {Box} from "@mui/material";
import {GridColDef} from '@mui/x-data-grid';
import ListComponent, {getDefaultBaseCriteria} from "@/app/components/common/ListComponent";
import {AlertContext} from "@/app/services/AlertService";
import {createIdsCriteria, findEntity} from "@/app/components/common/utils/ObjectUtils";
import {formatDateTime, getEntityPersonFullName} from "@/app/components/common/utils/BusinessUtils";
import {ServicesContext} from "@/app/services/ServiceProvider";

type ReceiptListProps = {
  create?: (callback: () => void) => void,
  view?: (id: number) => void
};

export default function ReceiptList(props: ReceiptListProps): React.ReactNode {
  const {
    receiptService,
    employeeService,
    customerCardService
  } = useContext(ServicesContext);
  const [items, setItems] = useState<Receipt[] | null>(null);
  const [criteria, setCriteria] = useState<ReceiptCriteria>(getDefaultBaseCriteria);
  const [employees, setEmployees] = useState<Employee[] | null>(null);
  const [customerCards, setCustomerCards] = useState<CustomerCard[] | null>(null);
  const showAlert = useContext(AlertContext);

  useEffect(() => {
    const fetch = async() => {
      const response = await employeeService.getEmployeeList({
        employeeCriteria: createIdsCriteria(items)
      });

      setEmployees(response.items);
    };

    fetch().catch(e => showAlert(e.toString(), "error"));
  }, [items]);
  useEffect(() => {
    const fetch = async() => {
      const response = await customerCardService.getCustomerCardList({
        customerCardCriteria: createIdsCriteria(items)
      });

      setCustomerCards(response.items);
    };

    fetch().catch(e => showAlert(e.toString(), "error"));
  }, [items]);

  async function fetch(): Promise<ReceiptListResponse> {
    return await receiptService.getReceiptList({ receiptCriteria: criteria });
  }

  async function handleDelete(id: number) {
    return await receiptService.deleteReceipt({ id });
  }

  function handleCreate(callback: () => void) {
    props.create?.(callback);
  }

  function handleView(id: number) {
    props.view?.(id);
  }

  const columns: GridColDef<Receipt>[] = [
    { field: "id", headerName: "ID", width: 80 },
    {
      field: "cashierId",
      headerName: "Касир",
      valueGetter: value=> getEntityPersonFullName(findEntity(employees, value)),
      width: 350
    },
    {
      field: "customerCardId",
      headerName: "Клієнт",
      valueGetter: value => value ? getEntityPersonFullName(findEntity(customerCards, value)) : "",
      width: 350
    },
    {
      field: "dateTime",
      headerName: "Дата",
      valueGetter: value => formatDateTime(value),
      width: 200
    },
    {
      field: "vat",
      headerName: "ПДВ",
      width: 100
    },
    {
      field: "totalPrice",
      headerName: "Вартість",
      width: 150
    }
  ];

  // TODO: Handle filters

  return (
    <ListComponent
      columns={columns}
      fetch={fetch}
      create={handleCreate}
      view={handleView}
      delete={handleDelete}
      criteria={criteria}
      setCriteria={setCriteria}

      items={items}
      setItems={setItems}
    />
  );
}
