import ApiAutocompleteComponent from "@/app/components/common/autocomplete/ApiAutocompleteComponent";
import {BaseCriteria, Product, ProductArchetype} from "../../../../../generated";
import {useContext, useEffect, useState} from "react";
import {ServicesContext} from "@/app/services/ServiceProvider";
import {getRequestError} from "@/app/components/common/utils/RequestUtils";
import {AlertContext} from "@/app/services/AlertService";
import {findEntity} from "@/app/components/common/utils/ObjectUtils";


type ProductAutocompleteProps = {
  initialId?: string,
  setSelectedId: (value: string | null) => void
};

export default function ProductAutocomplete(props: ProductAutocompleteProps) {
  const [items, setItems] = useState<Product[]>([]);
  const [productArchetypes, setProductArchetypes] = useState<ProductArchetype[]>([]);
  const { productService, productArchetypeService } = useContext(ServicesContext);
  const showAlert = useContext(AlertContext);

  useEffect(() => {
    const fetch = async() => {
      const response = await productArchetypeService.getProductArchetypeList({
        productArchetypeCriteria: {
          ids: items.map(item => item.archetype)
        }
      });

      setProductArchetypes(response.items);
    };

    fetch().catch(e => getRequestError(e).then(m => showAlert(m, "error")));
  }, [items]);

  async function fetch(criteria: BaseCriteria) {
    return await productService.getProductList({ productCriteria: criteria });
  }

  return (
    <ApiAutocompleteComponent
      initialId={props.initialId}
      setSelectedId={props.setSelectedId}
      fetch={fetch}
      label={"Товар"}
      getItemLabel={(item: Product) => item.id + " | " + findEntity(productArchetypes, item.archetype)?.name ?? ""}

      items={items}
      setItems={setItems}
    />
  );
}
