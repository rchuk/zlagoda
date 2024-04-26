import {FormControl, Grid, InputLabel, MenuItem, Select} from "@mui/material";
import ListFiltersComponent from "@/app/components/common/ListFiltersComponent";
import {EmployeeCriteria, EmployeeRole} from "../../../../generated";
import {EmployeeRole_i18} from "@/app/i18/EmployeeRole_i18";

type EmployeeFiltersProps = {
  criteria: EmployeeCriteria,
  setCriteria: (value: EmployeeCriteria) => void
};

export default function EmployeeFilters(props: EmployeeFiltersProps) {
  function setRole(value: string) {
    props.setCriteria({...props.criteria, role: value == "" ? undefined : value as EmployeeRole})
  }

  return (
    <ListFiltersComponent>
      <Grid item xs={3}>
        <FormControl fullWidth>
          <InputLabel>Посада</InputLabel>
          <Select
            label="Посада"
            required
            value={props.criteria.role ?? ""}
            onChange={e => setRole(e.target.value)}
          >
            <MenuItem key="null" value={""}>Усі посади</MenuItem>
            {Object.values(EmployeeRole).map(value => (
              <MenuItem key={value} value={value}>{EmployeeRole_i18[value]}</MenuItem>
            ))}
          </Select>
        </FormControl>
      </Grid>
    </ListFiltersComponent>
  );
}
