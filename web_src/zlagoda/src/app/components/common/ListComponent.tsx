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
import {getRequestError} from "@/app/components/common/utils/RequestUtils";
import {BaseEntity, EntityId} from "@/app/components/common/utils/ObjectUtils";
import {SEARCH_DEBOUNCE_MS} from "@/app/components/common/utils/Constants";

type ListToolbarProps = {
  createItem?: () => void
};

function ListToolbar(props: ListToolbarProps) {
  return (
    <GridToolbarContainer sx={{ display: "flex", justifyContent: "space-between", padding: 2 }}>
      <GridToolbarQuickFilter
        quickFilterParser={(input: string) => [input.trim()]}
        debounceMs={SEARCH_DEBOUNCE_MS}
      />
      {props.createItem &&
        <Button variant="outlined" startIcon={<AddIcon />} onClick={props.createItem}>
          Створити
        </Button>
      }
    </GridToolbarContainer>
  );
}

type ListComponentProps<ItemT extends GridValidRowModel & BaseEntity<IdT>, CriteriaT extends BaseCriteria, IdT extends EntityId> = {
  columns: GridColDef<ItemT>[],

  fetch: () => Promise<ListResponse & { items: ItemT[] }>,
  create?: (callback: () => void) => void,
  update?: (id: IdT, callback: () => void) => void,
  view?: (id: IdT) => void,

  delete?: (id: IdT) => Promise<boolean>,

  criteria: CriteriaT,
  setCriteria: (criteria: CriteriaT) => void,

  items?: ItemT[] | null,
  setItems?: (items: ItemT[] | null) => void,

  filters?: () => ReactElement
};

export function getDefaultBaseCriteria(): BaseCriteria {
  return {
    offset: 0,
    limit: 10
  };
}

export default function ListComponent<ItemT extends GridValidRowModel & BaseEntity<IdT>, CriteriaT extends BaseCriteria, IdT extends EntityId>
  (props: ListComponentProps<ItemT, CriteriaT, IdT>): React.ReactNode {
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

    fetch().catch(e => getRequestError(e).then(m => showAlert(m, "error")));
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
    const input: string = filter.quickFilterValues?.[0] ?? "";
    const query = input.trim() ?? undefined;

    props.setCriteria({...props.criteria, query});
  }

  function handleCreate() {
    props.create?.(fetchItems);
  }

  function handleView(id: IdT) {
    props.view?.(id);
  }

  function handleUpdate(id: IdT, callback: () => void) {
    props.update?.(id, callback);
  }

  function handleDelete(id: IdT) {
    const confirm = () => {
      const impl = async() => {
        const isSuccess = await props.delete?.(id);
        if (isSuccess)
          fetchItems();
      };

      impl()
        .then(() => showAlert("Інформацію успішно видалено", "success"))
        .catch(e => getRequestError(e).then(m => showAlert(m, "error")));
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
              onClick={() => handleView(id as IdT)}
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
              onClick={() => handleUpdate(id as IdT, fetchItems)}
              color="inherit"
            />
          ));
        }
        if (props.delete) {
          actions.push((
            <GridActionsCellItem
              icon={<DeleteIcon/>}
              label="Видалити"
              onClick={() => handleDelete(id as IdT)}
              color="inherit"
            />
          ));
        }

        return actions;
      }
    }
  ];

  return (
    <Box display="flex" flexDirection="column" width="100%" rowGap={2}>
      {props.filters && props.filters()}
      <DataGrid
        columns={columns}
        rows={items ?? []}
        paginationMode="server"
        rowCount={itemCount ?? 0}
        initialState={{
          pagination: {
            paginationModel: {
              pageSize: getDefaultBaseCriteria().limit
            }
          }
        }}
        onPaginationModelChange={onPaginationModelChange}
        pageSizeOptions={[10, 25, 50]}
        sortingMode="server"
        onSortModelChange={onSortModelChange}
        filterMode="server"
        onFilterModelChange={onFilterModelChange}
        disableColumnFilter
        slots={{
          toolbar: ListToolbar as GridSlots["toolbar"],
        }}
        slotProps={{
          toolbar: {
            createItem: props.create && handleCreate
          },
        }}
      />
    </Box>
  );
}
