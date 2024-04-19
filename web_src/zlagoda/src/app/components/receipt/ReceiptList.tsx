import {
  CustomerCard,
  CustomerCardApi, Employee,
  EmployeeApi,
  Receipt,
  ReceiptApi,
  ReceiptCriteria,
  ReceiptListResponse
} from "../../../../generated";
import React, {useContext, useEffect, useState} from "react";
import {Box} from "@mui/material";
import {GridColDef} from '@mui/x-data-grid';
import ListComponent, {getDefaultBaseCriteria} from "@/app/components/common/ListComponent";
import dayjs from "dayjs";
import {AlertContext} from "@/app/services/AlertService";
import {createIdsCriteria, findEntity} from "@/app/components/common/utils/ObjectUtils";

type ReceiptListProps = {
  receiptService: ReceiptApi,
  employeeService: EmployeeApi,
  customerCardService: CustomerCardApi
};

export default function ReceiptList(props: ReceiptListProps): React.ReactNode {
  const [items, setItems] = useState<Receipt[] | null>(null);
  const [criteria, setCriteria] = useState<ReceiptCriteria>(getDefaultBaseCriteria);
  const [employees, setEmployees] = useState<Employee[] | null>(null);
  const [customerCards, setCustomerCards] = useState<CustomerCard[] | null>(null);
  const showAlert = useContext(AlertContext);

  useEffect(() => {
    const fetch = async() => {
      const response = await props.employeeService.getEmployeeList({
        employeeCriteria: createIdsCriteria(items)
      });

      setEmployees(response.items);
    };

    fetch().catch(e => showAlert(e.toString(), "error"));
  }, [items]);
  useEffect(() => {
    const fetch = async() => {
      const response = await props.customerCardService.getCustomerCardList({
        customerCardCriteria: createIdsCriteria(items)
      });

      setCustomerCards(response.items);
    };

    fetch().catch(e => showAlert(e.toString(), "error"));
  }, [items]);

  async function fetch(): Promise<ReceiptListResponse> {
    return {
      totalCount: 2,
      items: [
        { id: 0, cashierId: 0, customerCardId: 66, dateTime: new Date(), vat: 100, totalPrice: 1500, items: []},
        { id: 55, cashierId: 2, dateTime: new Date(), vat: 5, totalPrice: 250, items: []},
      ]
    };

    // return await props.receiptService.getReceiptList({ receiptCriteria: criteria });
  }

  function handleCreate(callback: () => void) {

  }

  function handleView(id: number) {
  }

  function handleDelete(id: number, callback: () => void) {

  }

  // TODO: Create function for canonical name joining
  const columns: GridColDef<Receipt>[] = [
    { field: "id", headerName: "ID", width: 80 },
    {
      field: "cashierId",
      headerName: "Касир",
      valueGetter: value => {
        const employee = findEntity(employees, value);
        if (!employee)
          return "";

        return `${employee.lastName} ${employee.firstName}`;
      },
      width: 350
    },
    {
      field: "customCardId",
      headerName: "Клієнт",
      valueGetter: value => {
        if (!value)
          return "";

        const customerCard = findEntity(customerCards, value);
        if (!customerCard)
          return "";

        return `${customerCard.lastName} ${customerCard.firstName}`;
      },
      width: 350
    },
    {
      field: "dateTime",
      headerName: "Дата",
      valueGetter: value => dayjs(value).format("DD.MM.YYYY HH:mm:ss"),
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
    <Box>
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
    </Box>
  );
}
