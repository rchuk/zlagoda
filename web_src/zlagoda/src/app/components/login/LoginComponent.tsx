import {Box, Button, TextField, Typography} from "@mui/material";
import React, {useContext, useState} from "react";
import {getRequestError} from "@/app/components/common/utils/RequestUtils";
import {useRouter} from "next/router";
import {AlertContext} from "@/app/services/AlertService";
import {ResponseError} from "../../../../generated";


type LoginComponentProps = {

};

export default function LoginComponent(props: LoginComponentProps) {
  const [login, setLogin] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const showAlert = useContext(AlertContext);
  const router = useRouter();

  async function handleLogin() {
    const formData = new FormData();
    formData.append("username", login);
    formData.append("password", password);

    const response = await fetch("http://localhost:3333/api/token", {
      method: 'POST',
      body: formData,
    });

    if (!response.ok)
      throw new ResponseError(response);

    const data = await response.json();
    const token = data.token;
    console.log("token " + token);
  }

  function submit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();

    handleLogin()
      .then(_ => router.push("/"))
      .catch(e => getRequestError(e).then(m => showAlert(m, "error")));
  }

  return (
    <Box component="form" display="flex" flexDirection="column" rowGap={1} onSubmit={submit}>
      <Typography variant="h4" sx={{ marginBottom: 4 }}>
        Авторизація
      </Typography>
      <TextField label="Логін"
                 required
                 fullWidth
                 value={login}
                 onChange={e => setLogin(e.target.value)}
      />
      <TextField label="Пароль"
                 required
                 fullWidth
                 value={password}
                 onChange={e => setPassword(e.target.value)}
      />
      <Box display="flex" justifyContent="flex-end">
        <Button variant="outlined" type="submit">Увійти</Button>
      </Box>
    </Box>
  );
}
