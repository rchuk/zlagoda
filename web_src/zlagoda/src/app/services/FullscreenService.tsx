import React, {createContext, PropsWithChildren} from "react";
import {FullScreen, FullScreenHandle, useFullScreenHandle} from "react-full-screen";

export const FullscreenServiceContext = createContext<FullScreenHandle>(null!);

export type ServicesProviderProps = {

};

export default function FullscreenServiceProvider(props: PropsWithChildren<ServicesProviderProps>): React.ReactNode {
  const handle = useFullScreenHandle();

  return (
    <FullscreenServiceContext.Provider value={handle}>
      <FullScreen handle={handle}>
        {props.children}
      </FullScreen>
    </FullscreenServiceContext.Provider>
  );
}
