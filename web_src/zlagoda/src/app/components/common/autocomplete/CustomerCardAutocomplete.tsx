import ApiAutocompleteComponent from "@/app/components/common/autocomplete/ApiAutocompleteComponent";
import {BaseCriteria, CustomerCard} from "../../../../../generated";
import {useContext} from "react";
import {ServicesContext} from "@/app/services/ServiceProvider";
import {getEntityPersonFullName} from "@/app/components/common/utils/BusinessUtils";


type CustomerCardAutocompleteProps = {
  initialId?: string,
  setSelectedId: (value: string | null) => void
};

export default function CustomerCardAutocomplete(props: CustomerCardAutocompleteProps) {
  const { customerCardService } = useContext(ServicesContext);

  async function fetch(criteria: BaseCriteria) {
    return await customerCardService.getCustomerCardList({ customerCardCriteria: criteria });
  }

  return (
    <ApiAutocompleteComponent
      initialId={props.initialId}
      setSelectedId={props.setSelectedId}
      fetch={fetch}
      label={"Картка клієнта"}
      getItemLabel={(item: CustomerCard) => getEntityPersonFullName(item)}
    />
  );
}
