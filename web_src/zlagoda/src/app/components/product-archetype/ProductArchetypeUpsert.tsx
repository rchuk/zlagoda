import {
    ProductArchetypeView
} from "../../../../generated";
import React, {useCallback, useContext, useState} from "react";
import Grid from "@mui/material/Unstable_Grid2";
import {Autocomplete, TextField} from "@mui/material";
import UpsertComponent from "@/app/components/common/UpsertComponent";
import {ServicesContext} from "@/app/services/ServiceProvider";
import ProductCategoryAutocomplete from "@/app/components/common/autocomplete/ProductCategoryAutocomplete";

function getDefaultProductArchetypeView(): ProductArchetypeView {
    return {
        name: "",
        category: 0,
        manufacturer: "",
        description: ""
    };
}

type ProductArchetypeUpsertProps = {
    initialId: number | null,
    cancel?: () => void,
    onError?: () => void,
    onSave?: () => void
};

export default function ProductArchetypeUpsert(props: ProductArchetypeUpsertProps): React.ReactNode {
    const { productArchetypeService } = useContext(ServicesContext);
    const [view, setView] = useState<ProductArchetypeView>(getDefaultProductArchetypeView);

    const getBreadcrumb = useCallback(
      () => {
          return {
              title: view?.name ?? ""
          };
      },
      [view]
    );

    async function fetch(id: number) {
        setView(await productArchetypeService.getProductArchetypeById({id}));
    }

    async function create(): Promise<number> {
        return await productArchetypeService.createProductArchetype({productArchetypeView: view});
    }

    async function update(id: number) {
        await productArchetypeService.updateProductArchetype({id, productArchetypeView: view});
    }

    return (
        <UpsertComponent
            initialId={props.initialId}
            resetView={() => setView(getDefaultProductArchetypeView)}
            fetch={fetch}
            create={create}
            update={update}
            cancel={props.cancel}
            onError={props.onError}
            onSave={props.onSave}
            createHeader="Створення типу товару"
            updateHeader="Редагування типу товару"
            getBreadcrumb={getBreadcrumb}
        >
            <Grid xs={6}>
                <TextField label="Назва"
                           required
                           fullWidth
                           value={view.name}
                           onChange={e => setView({...view, name: e.target.value})}
                />
            </Grid>
            <Grid xs={6}>
                <ProductCategoryAutocomplete setSelectedId={v => setView({...view, category: v ?? 0})} />
            </Grid>

            <Grid xs={12}>
                <TextField label="Виробник"
                           required
                           fullWidth
                           value={view.manufacturer}
                           onChange={e => setView({...view, manufacturer: e.target.value})}
                />
            </Grid>
            <Grid xs={12}>
                <TextField label="Опис"
                           multiline
                           required
                           fullWidth
                           value={view.description}
                           onChange={e => setView({...view, description: e.target.value})}
                />
            </Grid>
        </UpsertComponent>
    );
}
