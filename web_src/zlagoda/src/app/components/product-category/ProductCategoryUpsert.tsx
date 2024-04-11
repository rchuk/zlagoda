import {ProductCategoryApi, ProductCategoryView} from "../../../../generated";
import React, {useState} from "react";
import {TextField} from "@mui/material";
import Grid from "@mui/material/Unstable_Grid2";
import UpsertComponent from "@/app/components/common/UpsertComponent";

function getDefaultProductCategoryView(): ProductCategoryView {
    return {
        name: ""
    };
}

type ProductCategoryUpsertProps = {
    initialId?: number,
    productCategoryService: ProductCategoryApi
};

export default function ProductCategoryUpsert(props: ProductCategoryUpsertProps): React.ReactNode {
    const [view, setView] = useState<ProductCategoryView>(getDefaultProductCategoryView);

    async function fetch() {
        const {id, ...newView} = await props.productCategoryService.getProductCategoryById({id: props.initialId!});
        setView(newView);
    }

    async function update(id: number) {
        await props.productCategoryService.updateProductCategory({id, productCategoryView: view});
    }

    async function create(): Promise<number> {
        return await props.productCategoryService.createProductCategory({productCategoryView: view});
    }

    function cancel() {

    }

    return (
        <UpsertComponent
            resetView={() => setView(getDefaultProductCategoryView)}
            fetch={fetch}
            create={create}
            update={update}
            cancel={cancel}
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
