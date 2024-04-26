import {CustomerCardCriteria} from "../../../../generated";
import ListFiltersComponent from "@/app/components/common/ListFiltersComponent";
import {TextField} from "@mui/material";
import Grid from "@mui/material/Unstable_Grid2";


/*
type CustomerCardFiltersProps = {
  criteria: CustomerCardCriteria,
  setCriteria: (value: CustomerCardCriteria) => void
};

function CustomerCardFilters(props: CustomerCardFiltersProps) {
  function setDiscountPercent(value: string) {
    props.setCriteria({
      ...props.criteria,
      discountPercent: value == "" ? null : Number(value)
    })
  }

  return (
    <ListFiltersComponent>
      <Grid item xs={3}>
        <TextField label="Відсоток знижки"
                   type="number"
                   required
                   inputProps={{min: 0, max: 100}}
                   fullWidth
                   value={props.criteria.discountPercent ?? ""}
                   onChange={e => setDiscountPercent(e.target.value)}
        />
      </Grid>
    </ListFiltersComponent>
  );
}
*/
