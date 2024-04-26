import {Card, CardActionArea, CardContent, Typography} from "@mui/material";
import {ReactElement} from "react";
import {useRouter} from "next/router";


type IconCardProps = {
  title: string,
  icon: (props: any) => ReactElement,
  link: string
};

export default function IconCard(props: IconCardProps) {
  const router = useRouter();

  function handleClick() {
    router.push(props.link);
  }

  return (
    <Card variant="outlined" sx={{ aspectRatio: 1 }}>
      <CardActionArea sx={{ display: "flex", flexDirection: "column", height: "100%", padding: 1 }} onClick={handleClick}>
        <Typography variant="h4" textAlign="center" fontSize="1.5rem" marginTop="20px">
          {props.title}
        </Typography>
        <CardContent sx={{ display: "flex", justifyContent: "center", alignItems: "center", padding: 0, margin: 0, flex: 1 }}>
          {props.icon({sx: { fontSize: "10vw" }})}
        </CardContent>
      </CardActionArea>
    </Card>
  );
}
