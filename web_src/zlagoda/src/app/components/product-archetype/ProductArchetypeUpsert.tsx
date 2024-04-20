import {
    ProductArchetypeView,
    ProductCategory
} from "../../../../generated";
import React, {useContext, useEffect, useMemo, useState} from "react";
import {AlertContext} from "@/app/services/AlertService";
import Grid from "@mui/material/Unstable_Grid2";
import {Autocomplete, TextField} from "@mui/material";
import UpsertComponent from "@/app/components/common/UpsertComponent";
import {findEntity} from "@/app/components/common/utils/ObjectUtils";
import {ServicesContext} from "@/app/services/ServiceProvider";

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
    onError?: () => void
};

export default function ProductArchetypeUpsert(props: ProductArchetypeUpsertProps): React.ReactNode {
    const { productArchetypeService, productCategoryService } = useContext(ServicesContext);
    const [view, setView] = useState<ProductArchetypeView>(getDefaultProductArchetypeView);
    const [productCategories, setProductCategories] = useState<Array<ProductCategory> | null>(null);
    const showAlert = useContext(AlertContext);

    // TODO: Deps might be wrong
    const selectedCategory = useMemo(
        () => findEntity(productCategories, view.category),
        [productCategories]
    );
    //

    useEffect(() => {
        const fetch = async() => {
            const newProductCategories = await productCategoryService.getProductCategoryList();
            setProductCategories(newProductCategories.items);
        };

        fetch().catch(e => showAlert(e.toString(), "error"));
    }, []);

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
                <Autocomplete
                    disablePortal
                    options={productCategories ?? []}
                    getOptionLabel={category => category.name}
                    fullWidth
                    renderInput={(params) => <TextField {...params} label="Категорія" />}
                    value={selectedCategory}
                    onChange={(_, v) => setView({...view, category: v?.id ?? 0})}
                />
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
