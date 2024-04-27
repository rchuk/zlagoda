import ApiAutocompleteComponent from "@/app/components/common/autocomplete/ApiAutocompleteComponent";
import {BaseCriteria, ProductCategory} from "../../../../../generated";
import {useContext} from "react";
import {ServicesContext} from "@/app/services/ServiceProvider";


type ProductCategoryAutocompleteProps = {
  initialId?: number,
  setSelectedId: (value: number | null) => void
};

export default function ProductCategoryAutocomplete(props: ProductCategoryAutocompleteProps) {
  const { productCategoryService } = useContext(ServicesContext);

  async function fetch(criteria: BaseCriteria) {
    return await productCategoryService.getProductCategoryList({ productCategoryCriteria: criteria });
  }

  return (
    <ApiAutocompleteComponent
      initialId={props.initialId}
      setSelectedId={props.setSelectedId}
      fetch={fetch}
      label={"Категорія товару"}
      getItemLabel={(item: ProductCategory) => item.name}
    />
  );
}
