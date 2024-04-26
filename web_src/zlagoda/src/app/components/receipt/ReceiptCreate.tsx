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

  // TODO: Create autocomplete components for products and customer cards (to enable proper search)

  const selectedProduct = useMemo(
    () => selectedProductId != null ? findEntity(products, selectedProductId) : null,
    [products]
  );

  useEffect(() => {
    const fetch = async() => {
      const response = await productService.getProductList();
      setProducts(response.items);
    };

    fetch().catch(e => getRequestError(e).then(m => showAlert(m, "error")));
  }, []);
  useEffect(() => {
    const fetch = async() => {
      const response = await productArchetypeService.getProductArchetypeList();
      setProductArchetypes(response.items);
    };

    fetch().catch(e => getRequestError(e).then(m => showAlert(m, "error")));
  }, []);

  async function create(): Promise<number> {
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

  // TODO: Get rid of double indirection
  return (
    <CreateComponent
      create={create}
      cancel={props.cancel}
      onSave={props.onSave}
      header="Створення чеку"
    >

      <Grid xs={12}>
        <Box display="flex" justifyContent="flex-end" columnGap={1}>
          <Autocomplete
            disablePortal
            options={products ?? []}
            getOptionLabel={product => findEntity(productArchetypes, product.archetype)!.name}
            fullWidth
            renderInput={(params) => <TextField {...params} label="Товар" />}
            value={selectedProduct}
            onChange={(_, v) => setSelectedProductId(v?.id ?? null)}
          />
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
