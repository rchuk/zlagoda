import { Box } from "@mui/material";
import Link from "next/link";
import React from "react";

export default function MainPage() {
  return (
    <Box display="flex" flexDirection="column" style={{ margin: 2 }}>
      <Link href="/customer-card">Картки клієнтів</Link>
      <Link href="/employee">Працівники</Link>
      <Link href="/receipt">Чеки</Link>
      <Link href="/product">Продукти</Link>
      <Link href="/product-archetype">Типи продуктів</Link>
      <Link href="/product-category">Категорії продуктів</Link>
    </Box>
  );
}
