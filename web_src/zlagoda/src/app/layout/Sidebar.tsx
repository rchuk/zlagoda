import {Drawer, IconButton, List, ListItem, ListItemButton, ListItemIcon, ListItemText, styled} from "@mui/material";
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import {ReactElement} from "react";
import {useRouter} from "next/router";
import {SIDEBAR_WIDTH} from "@/app/components/common/utils/Constants";
import {
  CustomerCardIcon, EmployeeIcon,
  ProductArchetypeIcon,
  ProductCategoryIcon,
  ProductIcon,
  ReceiptIcon
} from "@/app/components/common/Icons";


type SidebarProps = {
  isOpen: boolean,
  setIsOpen: (value: boolean) => void
}

const DrawerHeader = styled('div')(({ theme }) => ({
  display: 'flex',
  alignItems: 'center',
  padding: theme.spacing(0, 1),
  ...theme.mixins.toolbar,
  justifyContent: 'flex-end'
}));

type MenuItem = {
  name: string,
  link: string,
  icon: () => ReactElement
};

export default function Sidebar(props: SidebarProps) {
  const router = useRouter();

  const menuItems: MenuItem[] = [
    {
      name: "Картки клієнтів",
      link: "/customer-card",
      icon: CustomerCardIcon
    },
    {
      name: "Чеки",
      link: "/receipt",
      icon: ReceiptIcon
    },
    {
      name: "Продукти",
      link: "/product",
      icon: ProductIcon
    },
    {
      name: "Типи продуктів",
      link: "/product-archetype",
      icon: ProductArchetypeIcon
    },
    {
      name: "Категорії продуктів",
      link: "/product-category",
      icon: ProductCategoryIcon
    },
    {
      name: "Працівники",
      link: "/employee",
      icon: EmployeeIcon
    },
  ];

  function closeSidebar() {
    props.setIsOpen(false);
  }

  return (
    <Drawer
      sx={{
        width: SIDEBAR_WIDTH,
        flexShrink: 0,
        '& .MuiDrawer-paper': {
          width: SIDEBAR_WIDTH,
          boxSizing: 'border-box',
        }
      }}
      variant="persistent"
      anchor="left"
      open={props.isOpen}
    >
      <DrawerHeader>
        <IconButton onClick={closeSidebar}>
          <ChevronLeftIcon />
        </IconButton>
      </DrawerHeader>
      <List>
        {menuItems.map((item, index) => (
          <ListItem key={index} disablePadding>
            <ListItemButton onClick={() => router.push(item.link)}>
              <ListItemIcon>
                {item.icon()}
              </ListItemIcon>
              <ListItemText primary={item.name} />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    </Drawer>
  );
}
