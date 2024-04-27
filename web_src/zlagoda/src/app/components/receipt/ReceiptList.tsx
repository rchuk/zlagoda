import {
  CustomerCard,
  Employee,
  Receipt,
  ReceiptCriteria,
  ReceiptListResponse, UserRole
} from "../../../../generated";
import React, {useContext, useEffect, useState} from "react";
import {GridColDef} from '@mui/x-data-grid';
import ListComponent, {getDefaultBaseCriteria} from "@/app/components/common/ListComponent";
import {AlertContext} from "@/app/services/AlertService";
import {createStringIdsCriteria, findEntity} from "@/app/components/common/utils/ObjectUtils";
import {formatDateTime, getEntityPersonFullName} from "@/app/components/common/utils/BusinessUtils";
import {ServicesContext} from "@/app/services/ServiceProvider";
import {getRequestError} from "@/app/components/common/utils/RequestUtils";
import ReceiptFilters from "@/app/components/receipt/ReceiptFilters";
import {AuthServiceContext} from "@/app/services/AuthService";

type ReceiptListProps = {
  create?: (callback: () => void) => void,
  view?: (id: string) => void
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
  const authService = useContext(AuthServiceContext);

  useEffect(() => {
    const fetch = async() => {
      const response = await employeeService.getEmployeeList({
        employeeCriteria: {
          ids: items?.map(item => item.cashierId) ?? []
        }
      });

      setEmployees(response.items);
    };

    fetch().catch(e => getRequestError(e).then(m => showAlert(m, "error")));
  }, [items]);
  useEffect(() => {
    const fetch = async() => {
      const response = await customerCardService.getCustomerCardList({
        customerCardCriteria: {
          ids: items
            ?.map(item => item.customerCardId)
            .filter(id => id !== undefined) as string[] ?? []
        }
      });

      setCustomerCards(response.items);
    };

    fetch().catch(e => getRequestError(e).then(m => showAlert(m, "error")));
  }, [items]);

  async function fetch(): Promise<ReceiptListResponse> {
    return await receiptService.getReceiptList({ receiptCriteria: criteria });
  }

  async function handleDelete(id: string) {
    return await receiptService.deleteReceipt({ id });
  }

  function handleCreate(callback: () => void) {
    props.create?.(callback);
  }

  function handleView(id: string) {
    props.view?.(id);
  }

  const columns: GridColDef<Receipt>[] = [
    {
      field: "id",
      headerName: "ID",
      width: 120
    },
    {
      field: "cashierId",
      headerName: "Касир",
      valueGetter: (value: string)=> getEntityPersonFullName(findEntity(employees, value)),
      width: 300
    },
    {
      field: "customerCardId",
      headerName: "Клієнт",
      valueGetter: (value: string) => value ? getEntityPersonFullName(findEntity(customerCards, value)) : "",
      width: 300
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
      width: 120
    },
    {
      field: "totalPrice",
      headerName: "Вартість",
      width: 150
    }
  ];

  return (
    <ListComponent
      columns={columns}
      fetch={fetch}
      create={authService.hasRole(UserRole.Cashier) ? handleCreate : undefined}
      view={handleView}
      delete={authService.hasRole(UserRole.Manager) ? handleDelete : undefined}
      criteria={criteria}
      setCriteria={setCriteria}

      items={items}
      setItems={setItems}
      filters={() => <ReceiptFilters criteria={criteria} setCriteria={setCriteria} />}
    />
  );
}
