import {ProductArchetype, ProductCategory} from "../../../../generated";
import React, {useCallback, useContext, useState} from "react";
import ViewComponent from "@/app/components/common/ViewComponent";
import {ServicesContext} from "@/app/services/ServiceProvider";
import Link from "next/link";

type ProductArchetypeViewProps = {
    id: number,
    onError?: (reason: any) => void,
    edit?: (id: number) => void,
    cancel?: () => void
};

export default function ProductArchetypeView(props: ProductArchetypeViewProps): React.ReactNode {
    const { productArchetypeService, productCategoryService } = useContext(ServicesContext);
    const [productArchetype, setProductArchetype] = useState<ProductArchetype | null>(null);
    const [productCategory, setProductCategory] = useState<ProductCategory | null>(null);

    const getBreadcrumb = useCallback(
      () => {
          return {
              title: productArchetype?.name ?? ""
          };
      },
      [productArchetype]
    );

    async function fetch(id: number) {
        const newProductArchetype = await productArchetypeService.getProductArchetypeById({ id });
        setProductArchetype(newProductArchetype);
        setProductCategory(await productCategoryService.getProductCategoryById({ id: newProductArchetype.category }));
    }

    return (
        <ViewComponent id={props.id} fetch={fetch} onError={props.onError} edit={props.edit} cancel={props.cancel}
                       header="Перегляд типу товару" getBreadcrumb={getBreadcrumb}
        >
            <div>
                <b>Товар: </b><span>{productArchetype?.name}</span>
            </div>
            <div>
                <b>Категорія: </b>
                <Link href={`/product-category/${productArchetype?.category}`}>
                    {productCategory?.name}
                </Link>
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
