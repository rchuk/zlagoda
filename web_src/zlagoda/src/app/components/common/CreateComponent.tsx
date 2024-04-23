import React, {PropsWithChildren, useContext} from "react";
import UpsertContainer from "@/app/components/common/UpsertContainer";
import {AlertContext} from "@/app/services/AlertService";
import {getRequestError} from "@/app/components/common/utils/RequestUtils";
import {EntityId} from "@/app/components/common/utils/ObjectUtils";

type CreateComponentProps<IdT extends EntityId> = {
    create: () => Promise<IdT>,
    onSave?: () => void,
    cancel?: () => void,

    header: string
};

export default function CreateComponent<IdT extends EntityId>(props: PropsWithChildren<CreateComponentProps<IdT>>): React.ReactNode {
    const showAlert = useContext(AlertContext);

    function create() {
        const create = async() => {
            await props.create();
        }

        create()
            .then(_ => showAlert("Інформацію створено", "success"))
            .then(_ => props.onSave?.())
            .catch(e => getRequestError(e).then(m => showAlert(m, "error")));
    }

    function submit() {
        create()
    }

    function cancel() {
        props.cancel?.();
    }

    return (
        <UpsertContainer submit={submit} cancel={cancel} header={props.header}>
            {props.children}
        </UpsertContainer>
    );
}
