import {Autocomplete, debounce, TextField} from "@mui/material";
import {useContext, useEffect, useMemo, useState} from "react";
import {BaseEntity, EntityId, findEntity} from "@/app/components/common/utils/ObjectUtils";
import {SEARCH_DEBOUNCE_MS} from "@/app/components/common/utils/Constants";
import {BaseCriteria, ListResponse} from "../../../../../generated";
import {AlertContext} from "@/app/services/AlertService";
import {getRequestError} from "@/app/components/common/utils/RequestUtils";


function getDefaultBaseCriteria(): BaseCriteria {
  return {
    offset: 0,
    limit: 10
  };
}

type ApiAutocompleteComponentProps<ItemT extends BaseEntity<IdT>, IdT extends EntityId> = {
  setSelectedId: (value: IdT | null) => void,

  fetch: (criteria: BaseCriteria) => Promise<ListResponse & { items: ItemT[] }>,
  label: string,
  getItemLabel: (item: ItemT) => string
};

export default function ApiAutocompleteComponent<ItemT extends BaseEntity<IdT>, IdT extends EntityId>
  (props: ApiAutocompleteComponentProps<ItemT, IdT>) {
  const [items, setItems] = useState<ItemT[]>([]);
  const [inputValue, setInputValue] = useState<string>("");
  const [criteria, setCriteria] = useState<BaseCriteria>(getDefaultBaseCriteria);
  const [selectedItem, setSelectedItem] = useState<ItemT | null>(null);
  const showAlert = useContext(AlertContext);

  useEffect(() => {
    const fetch = async() => {
      const response = await props.fetch(criteria);

      setItems(response.items);
    };

    fetch().catch(e => getRequestError(e).then(m => showAlert(m, "error")));
  }, [criteria]);

  const searchDelayed = useMemo(
    () => debounce(() => setCriteria({...criteria, query: inputValue.trim()}), SEARCH_DEBOUNCE_MS),
    [inputValue]
  );

  return (
    <Autocomplete
      disablePortal
      fullWidth
      options={items}
      getOptionLabel={props.getItemLabel}
      value={selectedItem}
      onChange={(e, v) => setSelectedItem(v)}
      isOptionEqualToValue={(option, value) => option.id === value.id}
      inputValue={inputValue}
      onInputChange={(e, v) => {
        setInputValue(v);
        searchDelayed();
      }}
      filterOptions={x => x}
      renderInput={(params) => (
        <TextField {...params} label={props.label} variant="outlined" />
      )}
    />
  );
}
