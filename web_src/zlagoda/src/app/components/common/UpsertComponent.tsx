import React, {PropsWithChildren, useContext, useEffect, useState} from "react";
import UpsertContainer from "@/app/components/common/UpsertContainer";
import {AlertContext} from "@/app/services/AlertService";
import ProgressSpinner from "@/app/components/common/ProgressSpinner";
import {getRequestError} from "@/app/components/common/utils/RequestUtils";
import {EntityId} from "@/app/components/common/utils/ObjectUtils";

type UpsertComponentProps<IdT extends EntityId> = {
    initialId: IdT | null,
    createHeader: string,
    updateHeader: string,

    resetView: () => void,
    fetch: (id: IdT) => Promise<void>,
    create: () => Promise<IdT>,
    update: (id: IdT) => Promise<void>,
    onSave?: (id?: IdT) => void,
    cancel?: () => void,

    onError?: (reason: any) => void
};

export default function UpsertComponent<IdT extends EntityId>(props: PropsWithChildren<UpsertComponentProps<IdT>>): React.ReactNode {
    const [id, setId] = useState<IdT | null>(null);
    const [isReady, setIsReady] = useState<boolean>(false);
    const showAlert = useContext(AlertContext);

    useEffect(() => {
        if (props.initialId == null) {
            props.resetView();
            setIsReady(true);

            return;
        }

        const fetch = async() => {
            await props.fetch(props.initialId!)
        };

        setId(props.initialId);
        fetch()
          .then(_ => setIsReady(true))
          .catch(e => {
              getRequestError(e).then(m => showAlert(m, "error"))

              props.onError?.(e);
          });
    }, [props.initialId])

    function update() {
        const update = async() => {
            await props.update(id!);
        };

        update()
            .then(_ => showAlert("Інформацію оновлено", "success"))
            .then(_ => props.onSave?.(id!))
            .catch(e => getRequestError(e).then(m => showAlert(m, "error")));
    }

    function create() {
        const create = async() => {
            const id = await props.create();
            setId(id);

            return id;
        }

        create()
            .then(id => props.onSave?.(id))
            .then(_ => showAlert("Інформацію створено", "success"))
            .catch(e => getRequestError(e).then(m => showAlert(m, "error")));
    }

    function submit() {
        if (id == null)
            create()
        else
            update();
    }

    function cancel() {
        props.cancel?.();
    }

    if (!isReady)
        return <ProgressSpinner />;

    return (
        <UpsertContainer submit={submit} cancel={cancel} header={id != null ? props.updateHeader : props.createHeader}>
            {props.children}
        </UpsertContainer>
    );
}
