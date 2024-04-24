import {Product, ProductArchetype} from "../../../../generated";
import React, {useCallback, useContext, useState} from "react";
import ViewComponent from "@/app/components/common/ViewComponent";
import {Checkbox} from "@mui/material";
import {ServicesContext} from "@/app/services/ServiceProvider";


type ProductViewProps = {
    id: string,
    onError?: (reason: any) => void,
    edit?: (id: string) => void,
    cancel?: () => void
};

export default function ProductView(props: ProductViewProps): React.ReactNode {
    const { productService, productArchetypeService } = useContext(ServicesContext);
    const [product, setProduct] = useState<Product | null>(null);
    const [productArchetype, setProductArchetype] = useState<ProductArchetype | null>(null);

    const getBreadcrumb = useCallback(
      () => {
          return {
              title: productArchetype?.name ?? ""
          };
      },
      [productArchetype]
    );

    async function fetch(id: string) {
        const newProduct = await productService.getProductById({ id });
        setProduct(newProduct);
        setProductArchetype(await productArchetypeService.getProductArchetypeById({ id: newProduct.archetype }));
    }

    return (
        <ViewComponent id={props.id} fetch={fetch} onError={props.onError} edit={props.edit} cancel={props.cancel}
                       header="Перегляд товару" getBreadcrumb={getBreadcrumb}
        >
            <div>
                <b>UPC: </b><span>{product?.id}</span>
            </div>
            <div>
                <b>Назва: </b><span>{productArchetype?.name}</span>
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
