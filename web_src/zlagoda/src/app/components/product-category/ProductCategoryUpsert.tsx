import {ProductCategoryView} from "../../../../generated";
import React, {useContext, useState} from "react";
import {TextField} from "@mui/material";
import Grid from "@mui/material/Unstable_Grid2";
import UpsertComponent from "@/app/components/common/UpsertComponent";
import {ServicesContext} from "@/app/services/ServiceProvider";

function getDefaultProductCategoryView(): ProductCategoryView {
    return {
        name: ""
    };
}

type ProductCategoryUpsertProps = {
    initialId: number | null,
    cancel?: () => void,
    onError?: () => void
};

export default function ProductCategoryUpsert(props: ProductCategoryUpsertProps): React.ReactNode {
    const { productCategoryService } = useContext(ServicesContext);
    const [view, setView] = useState<ProductCategoryView>(getDefaultProductCategoryView);

    async function fetch() {
        const {id, ...newView} = await productCategoryService.getProductCategoryById({id: props.initialId!});
        setView(newView);
    }

    async function update(id: number) {
        await productCategoryService.updateProductCategory({id, productCategoryView: view});
    }

    async function create(): Promise<number> {
        return await productCategoryService.createProductCategory({productCategoryView: view});
    }

    return (
        <UpsertComponent
            initialId={props.initialId}
            resetView={() => setView(getDefaultProductCategoryView)}
            fetch={fetch}
            create={create}
            update={update}
            cancel={props.cancel}
            onError={props.onError}
            header={props.initialId != null ? "Редагування категорії товару" : "Створення категорії товару"}
        >
            <Grid xs={12}>
                <TextField label="Назва"
                           required
                           fullWidth
                           value={view.name}
                           onChange={e => setView({...view, name: e.target.value})}
                />
            </Grid>
        </UpsertComponent>
    );
}
