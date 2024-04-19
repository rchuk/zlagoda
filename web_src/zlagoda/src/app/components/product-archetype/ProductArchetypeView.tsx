import {ProductArchetype, ProductCategory} from "../../../../generated";
import React, {useContext, useState} from "react";
import ViewComponent from "@/app/components/common/ViewComponent";
import {ServicesContext} from "@/app/services/ServiceProvider";

type ProductArchetypeViewProps = {
    id: number
};

export default function ProductArchetypeView(props: ProductArchetypeViewProps): React.ReactNode {
    const { productArchetypeService, productCategoryService } = useContext(ServicesContext);
    const [productArchetype, setProductArchetype] = useState<ProductArchetype | null>(null);
    const [productCategory, setProductCategory] = useState<ProductCategory | null>(null);

    async function fetch(id: number) {
        setProductArchetype(await productArchetypeService.getProductArchetypeById({ id }));
        // TODO: Test
        setProductCategory(await productCategoryService.getProductCategoryById({ id: productArchetype!.category }));
    }

    // TODO: Add link to category
    return (
        <ViewComponent id={props.id} fetch={fetch}>
            <div>
                <b>Товар: </b><span>{productArchetype?.name}</span>
            </div>
            <div>
                <b>Категорія: </b><span>{productCategory?.name}</span>
            </div>
            <div>
                <b>Виробник: </b><span>{productArchetype?.manufacturer}</span>
            </div>
            <div>
                <b>Опис: </b><span>{productArchetype?.description}</span>
            </div>
        </ViewComponent>
    );
}
