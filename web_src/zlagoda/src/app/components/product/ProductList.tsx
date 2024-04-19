 import {
  Product,
  ProductApi, ProductArchetype, ProductArchetypeApi,
  ProductCriteria,
  ProductListResponse
} from "../../../../generated";
import React, {useContext, useEffect, useState} from "react";
import {Box, Checkbox} from "@mui/material";
import {GridColDef} from '@mui/x-data-grid';
import ListComponent, {getDefaultBaseCriteria} from "@/app/components/common/ListComponent";
 import {AlertContext} from "@/app/services/AlertService";

type ProductListProps = {
  productService: ProductApi,
  productArchetypeService: ProductArchetypeApi
};

export default function ProductList(props: ProductListProps): React.ReactNode {
  const [items, setItems] = useState<Product[] | null>(null);
  const [criteria, setCriteria] = useState<ProductCriteria>(getDefaultBaseCriteria);
  const [productArchetypes, setProductArchetypes] = useState<ProductArchetype[] | null>(null);
  const showAlert = useContext(AlertContext);

  useEffect(() => {
    const fetch = async() => {
      const response = await props.productArchetypeService.getProductArchetypeList({
        productArchetypeCriteria: {
          ids: items?.map(item => item.archetype) ?? []
        }
      });

      setProductArchetypes(response.items);
    };

    fetch().catch(e => showAlert(e.toString(), "error"));
  }, [items]);

  async function fetch(): Promise<ProductListResponse> {
    return {
      totalCount: 2,
      items: [
        { id: 0, upc: "12345", price: 100, archetype: 0, quantity: 10, hasDiscount: false },
        { id: 1, upc: "54321", price: 250, archetype: 1, quantity: 25, hasDiscount: true }
      ]
    };

    // return await props.productService.getProductList({ productCriteria: criteria });
  }

  function handleCreate(callback: () => void) {

  }

  function handleView(id: number) {

  }

  function handleUpdate(id: number) {

  }

  function handleDelete(id: number, callback: () => void) {

  }

  const columns: GridColDef<Product>[] = [
    { field: "id", headerName: "ID", width: 80 },
    {
      field: "archetype",
      valueGetter: value => {
        return productArchetypes?.find(archetype => archetype.id == value)?.name ?? ""
      },
      headerName: "Назва",
      width: 300
    },
    {
      field: "upc",
      headerName: "UPC",
      width: 200
    },
    {
      field: "hasDiscount",
      headerName: "Знижка",
      renderCell: ({ value }) => (<Checkbox checked={value ?? false} disableRipple />),
      width: 100
    },
    {
      field: "price",
      headerName: "Ціна",
      width: 150
    },
    {
      field: "quantity",
      headerName: "Кількість",
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
        update={handleUpdate}
        delete={handleDelete}
        criteria={criteria}
        setCriteria={setCriteria}

        items={items}
        setItems={setItems}
      />
    </Box>
  );
}
