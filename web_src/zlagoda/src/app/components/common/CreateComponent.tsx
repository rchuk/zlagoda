import React, {PropsWithChildren, useContext} from "react";
import UpsertContainer from "@/app/components/common/UpsertContainer";
import {AlertContext} from "@/app/services/AlertService";

type CreateComponentProps = {
    create: () => Promise<number>,
    onSave?: () => void,
    cancel: () => void
};

export default function CreateComponent(props: PropsWithChildren<CreateComponentProps>): React.ReactNode {
    const showAlert = useContext(AlertContext);

    function create() {
        const create = async() => {
            await props.create();
        }

        create()
            .then(_ => showAlert("Інформацію створено", "success"))
            .then(_ => props.onSave?.())
            .catch(e => showAlert(e.toString(), "error"));
    }

    function submit() {
        create()
    }

    function cancel() {
        props.cancel();
    }

    return (
        <UpsertContainer submit={submit} cancel={cancel}>
            {props.children}
        </UpsertContainer>
    );
}
