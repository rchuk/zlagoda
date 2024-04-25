import React from "react";
import IconCard from "@/app/components/common/IconCard";
import BasePage from "@/app/components/common/pages/BasePage";
import Grid from "@mui/material/Unstable_Grid2";
import { Navigation } from "@/app/layout/Navigation";

export default function MainPage() {
  const items = [
    Navigation.receipt,
    Navigation.customerCard,
    Navigation.product,
    Navigation.productArchetype,
    Navigation.productCategory,
    Navigation.employee
  ];

  return (
    <BasePage>
      <Grid container spacing={2}>
        {
          items
            .filter(item => item.isEnabled?.() ?? true)
            .map(item => (
              <Grid xs={4}>
                <IconCard title={item.title} icon={item.icon} link={item.path} />
              </Grid>
            ))
        }
      </Grid>
    </BasePage>
  );
}
