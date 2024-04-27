import {Product, ProductArchetype, ReceiptView, ReceiptItemView} from "../../../../generated";
import React, {useContext, useEffect, useMemo, useState} from "react";
import {AlertContext} from "@/app/services/AlertService";
import CreateComponent from "@/app/components/common/CreateComponent";
import Grid from "@mui/material/Unstable_Grid2";
import {ServicesContext} from "@/app/services/ServiceProvider";
import {findEntity} from "@/app/components/common/utils/ObjectUtils";
import {getRequestError} from "@/app/components/common/utils/RequestUtils";
import {Autocomplete, Box, Button, TextField} from "@mui/material";
import ReceiptItemCreate from "@/app/components/receipt/ReceiptItemCreate";
import CustomerCardAutocomplete from "@/app/components/common/autocomplete/CustomerCardAutocomplete";
import ProductAutocomplete from "@/app/components/common/autocomplete/ProductAutocomplete";

function getDefaultReceiptView(): ReceiptView {
  return {
    customerCardId: undefined,
    items: []
  };
}

type ReceiptCreateProps = {
  cancel?: () => void,
  onSave?: () => void
};

export default function ReceiptCreate(props: ReceiptCreateProps): React.ReactNode {
  const { receiptService, productService, productArchetypeService } = useContext(ServicesContext);
  const [view, setView] = useState<ReceiptView>(getDefaultReceiptView);
  const [products, setProducts] = useState<Product[] | null>(null);
  const [productArchetypes, setProductArchetypes] = useState<ProductArchetype[] | null>(null);
  const [selectedProductId, setSelectedProductId] = useState<string | null>(null);
  const showAlert = useContext(AlertContext);

  useEffect(() => {
    const fetch = async() => {
      const response = await productService.getProductList({
        productCriteria: {
          ids: view.items.map(item => item.product)
        }
      });
      setProducts(response.items);
    };

    fetch().catch(e => getRequestError(e).then(m => showAlert(m, "error")));
  }, [view.items]);
  useEffect(() => {
    const fetch = async() => {
      const response = await productArchetypeService.getProductArchetypeList({
        productArchetypeCriteria: {
          ids: products?.map(product => product.archetype)
        }
      });
      setProductArchetypes(response.items);
    };

    fetch().catch(e => getRequestError(e).then(m => showAlert(m, "error")));
  }, [products]);

  async function create(): Promise<string> {
    return await receiptService.createReceipt({receiptView: view});
  }

  function addItem() {
    if (selectedProductId == null)
      return;

    const newItem: ReceiptItemView = {
      product: selectedProductId,
      quantity: 1
    };
    const newItems = [...view.items, newItem];

    setView({...view, items: newItems});
    setSelectedProductId(null);
  }

  return (
    <CreateComponent
      create={create}
      cancel={props.cancel}
      onSave={props.onSave}
      header="Створення чеку"
    >
      <Grid xs={12}>
        <CustomerCardAutocomplete setSelectedId={v => setView({...view, customerCardId: v ?? undefined})}/>
      </Grid>
      <Grid xs={12}>
        <Box display="flex" justifyContent="flex-end" columnGap={1}>
          <ProductAutocomplete setSelectedId={v => setSelectedProductId(v)} />
          <Button variant="outlined" onClick={addItem}>Додати</Button>
        </Box>
        <Box display="flex" flexDirection="column">
          {
            view.items.map(item => (
              <ReceiptItemCreate
                view={view}
                setView={setView}
                product={item.product}
                productName={findEntity(productArchetypes, findEntity(products, item.product)!.archetype)!.name}
              />
            ))
          }
        </Box>
      </Grid>
    </CreateComponent>
  );
}
