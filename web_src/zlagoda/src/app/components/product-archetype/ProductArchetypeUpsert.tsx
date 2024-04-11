import {
    ProductArchetypeApi,
    ProductArchetypeView,
    ProductCategory,
    ProductCategoryApi,
} from "../../../../generated";
import React, {useContext, useEffect, useMemo, useState} from "react";
import {AlertContext} from "@/app/services/AlertService";
import Grid from "@mui/material/Unstable_Grid2";
import {Autocomplete, TextField} from "@mui/material";
import UpsertComponent from "@/app/components/common/UpsertComponent";

function getDefaultProductArchetypeView(): ProductArchetypeView {
    return {
        name: "",
        category: 0,
        manufacturer: "",
        description: ""
    };
}

type ProductArchetypeUpsertProps = {
    initialId?: number,
    productArchetypeService: ProductArchetypeApi,
    productCategoryService: ProductCategoryApi
};

export default function ProductArchetypeUpsert(props: ProductArchetypeUpsertProps): React.ReactNode {
    const [view, setView] = useState<ProductArchetypeView>(getDefaultProductArchetypeView);
    const [productCategories, setProductCategories] = useState<Array<ProductCategory> | null>(null);
    const showAlert = useContext(AlertContext);

    // TODO: Deps might be wrong
    const selectedCategory = useMemo(
        () => productCategories ? productCategories[view.category] : null,
        [productCategories]
    );
    //

    useEffect(() => {
        const fetch = async() => {
            const newProductCategories = await props.productCategoryService.getProductCategoryList();
            setProductCategories(newProductCategories);
        };

        // fetch().catch(e => showAlert(e.toString(), "error"));
    });

    async function fetch(id: number) {
        setView(await props.productArchetypeService.getProductArchetypeById({id}));
    }

    async function create(): Promise<number> {
        return await props.productArchetypeService.createProductArchetype({productArchetypeView: view});
    }

    async function update(id: number) {
        await props.productArchetypeService.updateProductArchetype({id, productArchetypeView: view});
    }

    function cancel() {

    }

    return (
        <UpsertComponent
            initialId={props.initialId}
            resetView={() => setView(getDefaultProductArchetypeView)}
            fetch={fetch}
            create={create}
            update={update}
            cancel={cancel}
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
