import {Grid,} from "@mui/material";
import ListFiltersComponent from "@/app/components/common/ListFiltersComponent";
import {ReceiptCriteria} from "../../../../generated";
import dayjs from "dayjs";
import {DateTimePicker} from "@mui/x-date-pickers";
import React from "react";
import EmployeeAutocomplete from "@/app/components/common/autocomplete/EmployeeAutocomplete";

type ReceiptFiltersProps = {
  criteria: ReceiptCriteria,
  setCriteria: (value: ReceiptCriteria) => void
};

export default function ReceiptFilters(props: ReceiptFiltersProps) {
  function setStartDate(value: dayjs.Dayjs | null) {
    props.setCriteria({...props.criteria, startDate: value?.toDate() ?? undefined })
  }

  function setEndDate(value: dayjs.Dayjs | null) {
    props.setCriteria({...props.criteria, endDate: value?.toDate() ?? undefined })
  }

  function setEmployee(value: string | null) {
    props.setCriteria({...props.criteria, cashierId: value ?? undefined});
  }

  return (
    <ListFiltersComponent>
      <Grid item xs={3}>
        <EmployeeAutocomplete setSelectedId={setEmployee} />
      </Grid>
      <Grid item xs={3}>
        <DateTimePicker label="Початкова дата"
                    disableFuture
                    slotProps={{
                      textField: { fullWidth: true },
                      actionBar: {
                        actions: ["clear"],
                      }
                    }}
                    value={props.criteria.startDate ? dayjs(props.criteria.startDate) : null}
                    onChange={value => setStartDate(value)}
        />
      </Grid>
      <Grid item xs={3}>
        <DateTimePicker label="Кінцева дата"
                    disableFuture
                    slotProps={{
                      textField: { fullWidth: true },
                      actionBar: {
                        actions: ["clear"],
                      }
                    }}
                    value={props.criteria.endDate ? dayjs(props.criteria.endDate) : null}
                    onChange={value => setEndDate(value)}
        />
      </Grid>
    </ListFiltersComponent>
  );
}

