import {Box, Paper} from "@mui/material";


export default function Header() {
  return (
    <Paper sx={{
      position: "sticky", top: "0", alignSelf: "flex-start", minHeight: "100px", display: "flex", alignItems: "center",
      zIndex: "999", width: "100%"
    }}>
      <h1 style={{ marginLeft: 15 }}>Злагода</h1>
    </Paper>
  );
}
