import React, {createContext, PropsWithChildren, useCallback, useState} from "react";
import {UserRole} from "../../../generated";

export type AuthData = {
  token: string | null,
  setToken: (value: string | null) => void,

  role: UserRole | null,
  setRole: (value: UserRole | null) => void,
  hasRole: (role: UserRole) => boolean,

  employeeId: string | null,
  setEmployeeId: (value: string | null) => void,

  logout: () => void
};

export const AuthServiceContext = createContext<AuthData>(null!);

type AuthServiceProviderProps = {
  token: string | null,
  setToken: (value: string | null) => void
};

export default function AuthServiceProvider(props: PropsWithChildren<AuthServiceProviderProps>) {
  const [role, setRole] = useState<UserRole | null>(null);
  const [employeeId, setEmployeeId] = useState<string | null>(null);

  const hasRole = useCallback((value: UserRole) => {
    return true; // TODO
  }, []);

  function setToken(value: string | null) {
    localStorage.setItem("access-token", value ?? "");
    props.setToken(value);
  }

  function logout() {
    setToken(null);
    setRole(null);
  }

  const data: AuthData = {
    token: props.token,
    setToken,
    role,
    setRole,
    hasRole,
    logout,
    employeeId,
    setEmployeeId
  };

  return (
    <AuthServiceContext.Provider value={data}>
      {props.children}
    </AuthServiceContext.Provider>
  );
}
