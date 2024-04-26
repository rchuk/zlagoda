import {
  CustomerCardIcon,
  EmployeeIcon, ExtraQueryIcon,
  ProductArchetypeIcon, ProductCategoryIcon,
  ProductIcon,
  ReceiptIcon, UserIcon
} from "@/app/components/common/Icons";
import {ReactElement} from "react";
import HomeIcon from "@mui/icons-material/Home";


export type NavigationItem = {
  title: string,
  path: string,
  icon: () => ReactElement,
  isEnabled?: () => boolean
};

export const Navigation: Record<string, NavigationItem> = {
  main: {
    title: "Головна",
    path: "/",
    icon: () => (<HomeIcon />)
  },
  receipt: {
    title: "Чеки",
    path: "/receipt",
    icon: ReceiptIcon
  },
  customerCard: {
    title: "Картки клієнтів",
    path: "/customer-card",
    icon: CustomerCardIcon
  },
  product: {
    title: "Товари",
    path: "/product",
    icon: ProductIcon
  },
  productArchetype: {
    title: "Типи товарів",
    path: "/product-archetype",
    icon: ProductArchetypeIcon
  },
  productCategory: {
    title: "Категорії товарів",
    path: "/product-category",
    icon: ProductCategoryIcon
  },
  employee: {
    title: "Працівники",
    path: "/employee",
    icon: EmployeeIcon,
    isEnabled: () => true
  },
  users: {
    title: "Користувачі",
    path: "/user",
    icon: UserIcon
  },
  extraQuery: {
    title: "Додаткові запити",
    path: "/extra-query",
    icon: ExtraQueryIcon
  }
};
