import React, {createContext, PropsWithChildren, useCallback, useState} from "react";
import {UserRole} from "../../../generated";

export type AuthData = {
  token: string | null,
  setToken: (value: string | null) => void,

  role: UserRole | null,
  setRole: (value: UserRole | null) => void,
  hasRole: (role: UserRole) => boolean
};

export const AuthServiceContext = createContext<AuthData>(null!);

type AuthServiceProviderProps = {
  token: string | null,
  setToken: (value: string | null) => void
};

export default function AuthServiceProvider(props: PropsWithChildren<AuthServiceProviderProps>) {
  const [role, setRole] = useState<UserRole | null>(null);

  const hasRole = useCallback((value: UserRole) => {
    return true; // TODO
  }, []);

  const data: AuthData = {
    token: props.token,
    setToken: props.setToken,
    role,
    setRole,
    hasRole
  };

  return (
    <AuthServiceContext.Provider value={data}>
      {props.children}
    </AuthServiceContext.Provider>
  );
}
