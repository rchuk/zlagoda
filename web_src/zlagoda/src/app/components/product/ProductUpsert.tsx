import {ProductApi, ProductArchetype, ProductArchetypeApi, ProductView} from "../../../../generated";
import React, {useContext, useEffect, useMemo, useState} from "react";
import {AlertContext} from "@/app/services/AlertService";
import UpsertComponent from "@/app/components/common/UpsertComponent";
import Grid from "@mui/material/Unstable_Grid2";
import {Autocomplete, TextField} from "@mui/material";
import {findEntity} from "@/app/components/common/utils/ObjectUtils";

function getDefaultProductView(): ProductView {
    return {
        archetype: 0,
        upc: "",
        price: 0,
        quantity: 0
    };
}

type ProductUpsertProps = {
    initialId?: number,
    productService: ProductApi,
    productArchetypeService: ProductArchetypeApi
};

export default function ProductUpsert(props: ProductUpsertProps): React.ReactNode {
    const [view, setView] = useState<ProductView>(getDefaultProductView);
    const [productArchetypes, setProductArchetypes] = useState<ProductArchetype[] | null>(null);
    const showAlert = useContext(AlertContext);

    // TODO: Test
    const selectedArchetype = useMemo(
        () => findEntity(productArchetypes, view.archetype),
        [productArchetypes]
    );

    useEffect(() => {
        const fetch = async() => {
            const response = await props.productArchetypeService.getProductArchetypeList();
            setProductArchetypes(response.items);
        };

        fetch().catch(e => showAlert(e.toString(), "error"));
    });

    async function fetch(id: number) {
        setView(await props.productService.getProductById({id}));
    }

    async function create(): Promise<number> {
        return await props.productService.createProduct({productView: view});
    }

    async function update(id: number) {
        await props.productService.updateProdact({id, productView: view});
    }

    function cancel() {

    }

    return (
        <UpsertComponent
            initialId={props.initialId}
            resetView={() => setView(getDefaultProductView)}
            fetch={fetch}
            create={create}
            update={update}
            cancel={cancel}
        >
            <Grid xs={6}>
                <Autocomplete
                    disablePortal
                    options={productArchetypes ?? []}
                    getOptionLabel={archetype => archetype.name}
                    fullWidth
                    renderInput={(params) => <TextField {...params} label="Товар" />}
                    value={selectedArchetype}
                    onChange={(_, v) => setView({...view, archetype: v?.id ?? 0})}
                />
            </Grid>
            <Grid xs={6}>
                <TextField label="UPC"
                           required
                           fullWidth
                           value={view.upc}
                           onChange={e => setView({...view, upc: e.target.value})}
                />
            </Grid>
            <Grid xs={6}>
                <TextField label="Ціна"
                           type="number"
                           required
                           inputProps={{min: 0}}
                           fullWidth
                           value={view.price}
                           onChange={e => setView({...view, price: Number(e.target.value)})}
                />
            </Grid>
            <Grid xs={6}>
                <TextField label="Кількість"
                           type="number"
                           required
                           inputProps={{min: 0}}
                           fullWidth
                           value={view.quantity}
                           onChange={e => setView({...view, quantity: Number(e.target.value)})}
                />
            </Grid>
        </UpsertComponent>
    );
}
