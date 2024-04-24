import {Box, Button, TextField} from "@mui/material";
import React, {useState} from "react";
import BasePage from "@/app/components/common/pages/BasePage";


type LoginComponentProps = {

};

export default function LoginComponent(props: LoginComponentProps) {
  const [login, setLogin] = useState<string>();
  const [password, setPassword] = useState<string>();

  return (
    <BasePage>
      <Box component="form" display="flex" flexDirection="column" rowGap={1}>
        <h1 style={{ textAlign: "center" }}>Авторизація</h1>
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
    </BasePage>
  );
}
