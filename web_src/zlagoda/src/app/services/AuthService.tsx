import React, {createContext, PropsWithChildren, useCallback} from "react";
import {UserRole} from "../../../generated";

export type AuthData = {
  token: string | null,
  setToken: (value: string | null) => void,

  hasRole: (role: UserRole) => boolean
};

export const AuthServiceContext = createContext<AuthData>(null!);

type AuthServiceProviderProps = {
  token: string | null,
  setToken: (value: string | null) => void
};

export default function AuthServiceProvider(props: PropsWithChildren<AuthServiceProviderProps>) {
  const hasRole = useCallback((value: UserRole) => {
    return true; // TODO
  }, []);

  return (
    <AuthServiceContext.Provider value={{ token: props.token, setToken: props.setToken, hasRole }}>
      {props.children}
    </AuthServiceContext.Provider>
  );
}
