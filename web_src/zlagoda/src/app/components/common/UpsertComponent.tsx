import React, {PropsWithChildren, useContext, useEffect, useState} from "react";
import UpsertContainer from "@/app/components/common/UpsertContainer";
import {AlertContext} from "@/app/services/AlertService";
import ProgressSpinner from "@/app/components/common/ProgressSpinner";

type UpsertComponentProps = {
    initialId: number | null,
    header: string,

    resetView: () => void,
    fetch: (id: number) => Promise<void>,
    create: () => Promise<number>,
    update: (id: number) => Promise<void>,
    onSave?: () => void,
    cancel?: () => void,

    onError?: (reason: any) => void
};

export default function UpsertComponent(props: PropsWithChildren<UpsertComponentProps>): React.ReactNode {
    const [id, setId] = useState<number | null>(null);
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
              showAlert(`Помилка при отриманні інформації.\n${e.toString()}`, "error");

              props.onError?.(e);
          });
    }, [props.initialId])

    function update() {
        const update = async() => {
            await props.update(id!);
        };

        update()
            .then(_ => showAlert("Інформацію оновлено", "success"))
            .then(_ => props.onSave?.())
            .catch(e => showAlert(e.toString(), "error"));
    }

    function create() {
        const create = async() => {
            const id = await props.create();
            setId(id);
        }

        create()
            .then(_ => showAlert("Інформацію створено", "success"))
            .then(_ => props.onSave?.())
            .catch(e => showAlert(e.toString(), "error"));
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
        <UpsertContainer submit={submit} cancel={cancel} header={props.header}>
            {props.children}
        </UpsertContainer>
    );
}
