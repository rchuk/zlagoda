import ApiAutocompleteComponent from "@/app/components/common/autocomplete/ApiAutocompleteComponent";
import {BaseCriteria, ProductArchetype} from "../../../../../generated";
import {useContext} from "react";
import {ServicesContext} from "@/app/services/ServiceProvider";


type ProductArchetypeAutocompleteProps = {
  initialId?: number,
  setSelectedId: (value: number | null) => void
};

export default function ProductArchetypeAutocomplete(props: ProductArchetypeAutocompleteProps) {
  const { productArchetypeService } = useContext(ServicesContext);

  async function fetch(criteria: BaseCriteria) {
    return await productArchetypeService.getProductArchetypeList({ productArchetypeCriteria: criteria });
  }

  return (
    <ApiAutocompleteComponent
      initialId={props.initialId}
      setSelectedId={props.setSelectedId}
      fetch={fetch}
      label={"Тип товару"}
      getItemLabel={(item: ProductArchetype) => item.name}
    />
  );
}
