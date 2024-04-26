import React, {PropsWithChildren, useContext, useEffect, useState} from "react";
import UpsertContainer from "@/app/components/common/UpsertContainer";
import {AlertContext} from "@/app/services/AlertService";
import ProgressSpinner from "@/app/components/common/ProgressSpinner";
import {getRequestError} from "@/app/components/common/utils/RequestUtils";
import {EntityId} from "@/app/components/common/utils/ObjectUtils";
import {BreadcrumbItem} from "@/app/components/common/BreadcrumbsComponent";
import {BreadcrumbsServiceContext} from "@/app/services/BreadcrumbsService";

type UpsertComponentProps<IdT extends EntityId> = {
    initialId: IdT | null,
    createHeader: string,
    updateHeader: string,

    resetView: () => void,
    fetch: (id: IdT) => Promise<void>,
    create: () => Promise<IdT>,
    update: (id: IdT) => Promise<void>,

    onSave?: () => void,
    cancel?: () => void,
    onError?: (reason: any) => void,

    getBreadcrumb?: () => BreadcrumbItem
};

export default function UpsertComponent<IdT extends EntityId>(props: PropsWithChildren<UpsertComponentProps<IdT>>): React.ReactNode {
    const [id, setId] = useState<IdT | null>(null);
    const [isReady, setIsReady] = useState<boolean>(false);
    const [isDirty, setIsDirty] = useState<boolean>(true);
    const showAlert = useContext(AlertContext);
    const breadcrumbsHandle = useContext(BreadcrumbsServiceContext);

    useEffect(() => {
        if (!isDirty) {
            if (props.getBreadcrumb !== undefined)
                breadcrumbsHandle.modify(props.getBreadcrumb());

            setIsDirty(true);
        }
    }, [isDirty]);

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
          .then(_ => {
              setIsDirty(false);
              setIsReady(true);
          })
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
            .then(_ => setIsDirty(false))
            .then(_ => props.onSave?.())
            .catch(e => getRequestError(e).then(m => showAlert(m, "error")));
    }

    function create() {
        const create = async() => {
            const id = await props.create();
            setId(id);

            return id;
        }

        create()
            .then(_ => showAlert("Інформацію створено", "success"))
            .then(_ => setIsDirty(false))
            .then(id => props.onSave?.())
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
