import {Product, ProductArchetype} from "../../../../generated";
import React, {useContext, useState} from "react";
import ViewComponent from "@/app/components/common/ViewComponent";
import {Checkbox} from "@mui/material";
import {ServicesContext} from "@/app/services/ServiceProvider";


type ProductViewProps = {
    id: number
};

export default function ProductView(props: ProductViewProps): React.ReactNode {
    const { productService, productArchetypeService } = useContext(ServicesContext);
    const [product, setProduct] = useState<Product | null>(null);
    const [productArchetype, setProductArchetype] = useState<ProductArchetype | null>(null);

    async function fetch(id: number) {
        setProduct(await productService.getProductById({ id }));
        // TODO: Test
        setProductArchetype(await productArchetypeService.getProductArchetypeById({ id: product!.id }));
    }

    // TODO: Add link to archetype
    return (
        <ViewComponent id={props.id} fetch={fetch}>
            <div>
                <b>Назва: </b><span>{productArchetype?.name}</span>
            </div>
            <div>
                <b>UPC: </b><span>{product?.upc}</span>
            </div>
            <div>
                <b>Ціна: </b><span>{product?.price}</span>
            </div>
            <div>
                <b>Кількість: </b><span>{product?.quantity}</span>
            </div>
            <div>
                <b>Знижка: </b><Checkbox disabled value={product?.hasDiscount}/>
            </div>
        </ViewComponent>
    );
}
