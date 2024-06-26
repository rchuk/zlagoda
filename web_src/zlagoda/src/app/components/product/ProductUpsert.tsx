import {ProductArchetype, ProductView} from "../../../../generated";
import React, {useCallback, useContext, useEffect, useMemo, useState} from "react";
import {AlertContext} from "@/app/services/AlertService";
import UpsertComponent from "@/app/components/common/UpsertComponent";
import Grid from "@mui/material/Unstable_Grid2";
import {TextField} from "@mui/material";
import {findEntity} from "@/app/components/common/utils/ObjectUtils";
import {ServicesContext} from "@/app/services/ServiceProvider";
import {getRequestError} from "@/app/components/common/utils/RequestUtils";
import ProductArchetypeAutocomplete from "@/app/components/common/autocomplete/ProductArchetypeAutocomplete";

function getDefaultProductView(): ProductView {
    return {
        id: "",
        archetype: 0,
        price: 0,
        quantity: 0
    };
}

type ProductUpsertProps = {
    initialId: string | null,
    cancel?: () => void,
    onError?: () => void,
    onSave?: () => void
};

export default function ProductUpsert(props: ProductUpsertProps): React.ReactNode {
    const { productService, productArchetypeService } = useContext(ServicesContext);
    const [view, setView] = useState<ProductView>(getDefaultProductView);
    const [archetype, setArchetype] = useState<ProductArchetype>();
    const showAlert = useContext(AlertContext);

    const getBreadcrumb = useCallback(
      () => {
        return {
            title: archetype?.name ?? ""
        };
      },
      [archetype]
    );

    useEffect(() => {
        if (view.archetype == 0)
            return;

        const fetch = async() => {
            const response = await productArchetypeService.getProductArchetypeById({ id: view.archetype });
            setArchetype(response);
        };

        fetch().catch(e => getRequestError(e).then(m => showAlert(m, "error")));
    }, [view.archetype]);

    async function fetch(id: string) {
        setView( await productService.getProductById({id}));
    }

    async function create(): Promise<string> {
        return await productService.createProduct({productView: view});
    }

    async function update(id: string) {
        await productService.updateProdact({id, productView: view});
    }

    return (
        <UpsertComponent
            initialId={props.initialId}
            resetView={() => setView(getDefaultProductView)}
            fetch={fetch}
            create={create}
            update={update}
            cancel={props.cancel}
            onError={props.onError}
            onSave={props.onSave}
            createHeader="Створення товару"
            updateHeader="Редагування товару"
            getBreadcrumb={getBreadcrumb}
        >
            <Grid xs={6}>
                <TextField label="UPC"
                           required
                           fullWidth
                           value={view.id}
                           disabled={props.initialId != null}
                           onChange={e => setView({...view, id: e.target.value})}
                />
            </Grid>
            <Grid xs={6}>
                <ProductArchetypeAutocomplete initialId={view.archetype} setSelectedId={v => setView({...view, archetype: v ?? 0})} />
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
