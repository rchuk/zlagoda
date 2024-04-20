import React, {ReactElement, useContext, useEffect, useState} from "react";
import {AlertContext} from "@/app/services/AlertService";
import {Box, Button} from "@mui/material";
import {BaseCriteria, ListResponse} from "../../../../generated";
import {
  DataGrid, GridActionsCellItem,
  GridColDef,
  GridFilterModel,
  GridPaginationModel, GridRowParams,
  GridSlots,
  GridSortModel, GridToolbarContainer, GridToolbarQuickFilter,
  GridValidRowModel
} from "@mui/x-data-grid";
import AddIcon from "@mui/icons-material/Add";
import VisibilityIcon from '@mui/icons-material/Visibility';
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";
import {ConfirmationDialogContext} from "@/app/services/ConfirmationDialogService";

type ListToolbarProps = {
  createItem?: () => void
};

function ListToolbar(props: ListToolbarProps) {
  return (
    <GridToolbarContainer sx={{display: "flex", justifyContent: "space-between"}}>
      <GridToolbarQuickFilter />
      {props.createItem &&
        <Button color="primary" startIcon={<AddIcon />} onClick={props.createItem}>
          Створити
        </Button>
      }
    </GridToolbarContainer>
  );
}

// NOTE: Callback is only needed for create if it's implemented with modal
type ListComponentProps<ItemT extends GridValidRowModel, CriteriaT extends BaseCriteria> = {
  columns: GridColDef<ItemT>[],

  fetch: () => Promise<ListResponse & { items: ItemT[] }>,
  create?: (callback: () => void) => void,
  update?: (id: number) => void,
  view?: (id: number) => void,

  delete?: (id: number) => Promise<boolean>,

  criteria: CriteriaT,
  setCriteria: (criteria: CriteriaT) => void,
  setFilter?: (filter: GridFilterModel) => void,

  items?: ItemT[] | null,
  setItems?: (items: ItemT[] | null) => void
};

export function getDefaultBaseCriteria(): BaseCriteria {
  return {
    offset: 0,
    limit: 10
  };
}

export default function ListComponent<ItemT extends GridValidRowModel, CriteriaT extends BaseCriteria>(props: ListComponentProps<ItemT, CriteriaT>): React.ReactNode {
  const [itemsInternal, setItemsInternal] = useState<ItemT[] | null>(null);
  const [itemCount, setItemCount] = useState<number | null>(null);
  const showAlert = useContext(AlertContext);
  const showConfirmation = useContext(ConfirmationDialogContext);

  const items = props.items || itemsInternal;
  const setItems = props.setItems || setItemsInternal;

  function fetchItems() {
    const fetch = async() => {
      const response = await props.fetch();
      setItemCount(response.totalCount);
      setItems(response.items);
    }

    fetch().catch(e => showAlert(e.toString(), "error"));
  }

  useEffect(() => {
    fetchItems();
  }, [props.criteria]);

  function onPaginationModelChange(pagination: GridPaginationModel) {
    props.setCriteria({...props.criteria, offset: pagination.page * pagination.pageSize, limit: pagination.pageSize});
  }

  function onSortModelChange(sort: GridSortModel) {
    // TODO: Test
    const sortData = sort[0] ?? null
    const sortField = sortData?.field;
    const sortAscending = sortData?.sort != "desc";

    props.setCriteria({...props.criteria, sortField, sortAscending});
  }

  function onFilterModelChange(filter: GridFilterModel) {
    props.setFilter?.(filter);
  }

  function handleCreate() {
    props.create?.(fetchItems);
  }

  function handleView(id: number) {
    props.view?.(id);
  }

  function handleUpdate(id: number) {
    props.update?.(id);
  }

  function handleDelete(id: number) {
    const confirm = () => {
      const impl = async() => {
        const isSuccess = await props.delete?.(id);
        if (isSuccess)
          fetchItems();
      };

      impl().catch(e => showAlert(e.toString(), "error"));
    };

    showConfirmation({ confirm });
  }

  const columns: GridColDef<ItemT>[] = [
    ...props.columns,
    {
      field: "actions",
      type: "actions",
      headerName: "Дії",
      width: 150,
      cellClassName: "actions",
      getActions: ({id}: GridRowParams) => {
        let actions: ReactElement[] = [];

        if (props.view) {
          actions.push((
            <GridActionsCellItem
              icon={<VisibilityIcon/>}
              label="Переглянути"
              className="textPrimary"
              onClick={() => handleView(id as number)}
              color="inherit"
            />
          ));
        }
        if (props.update) {
          actions.push((
            <GridActionsCellItem
              icon={<EditIcon/>}
              label="Редагувати"
              className="textPrimary"
              onClick={() => handleUpdate(id as number)}
              color="inherit"
            />
          ));
        }
        if (props.delete) {
          actions.push((
            <GridActionsCellItem
              icon={<DeleteIcon/>}
              label="Видалити"
              onClick={() => handleDelete(id as number)}
              color="inherit"
            />
          ));
        }

        return actions;
      }
    }
  ];

  return (
    <DataGrid
      sx={{ margin: 2 }}

      columns={columns}
      rows={items ?? []}
      paginationMode="server"
      rowCount={itemCount ?? 0}
      onPaginationModelChange={onPaginationModelChange}
      pageSizeOptions={[10, 25, 50]}
      sortingMode="server"
      onSortModelChange={onSortModelChange}
      filterMode="server"
      disableColumnFilter={!props.setFilter}
      onFilterModelChange={onFilterModelChange}
      slots={{
        toolbar: ListToolbar as GridSlots["toolbar"],
      }}
      slotProps={{
        toolbar: {
          createItem: props.create && handleCreate
        },
      }}
    />
  );
}
