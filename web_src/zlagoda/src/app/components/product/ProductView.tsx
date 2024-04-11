import {Product, ProductApi, ProductArchetype, ProductArchetypeApi} from "../../../../generated";
import React, {useState} from "react";
import ViewComponent from "@/app/components/common/ViewComponent";
import {Checkbox} from "@mui/material";


type ProductViewProps = {
    id: number,
    productService: ProductApi,
    productArchetypeService: ProductArchetypeApi
};

export default function ProductView(props: ProductViewProps): React.ReactNode {
    const [product, setProduct] = useState<Product | null>(null);
    const [productArchetype, setProductArchetype] = useState<ProductArchetype | null>(null);

    async function fetch(id: number) {
        setProduct(await props.productService.getProductById({ id }));
        // TODO: Test
        setProductArchetype(await props.productArchetypeService.getProductArchetypeById({ id: product!.id }));
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
