import {
  Divider,
  Drawer,
  IconButton,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  styled
} from "@mui/material";
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import {ReactElement} from "react";
import {useRouter} from "next/router";
import {SIDEBAR_WIDTH} from "@/app/components/common/utils/Constants";
import {
  CustomerCardIcon, EmployeeIcon, ExtraQueryIcon,
  ProductArchetypeIcon,
  ProductCategoryIcon,
  ProductIcon,
  ReceiptIcon, UserIcon
} from "@/app/components/common/Icons";


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
  icon: () => ReactElement,
  enableIf?: () => boolean
};

type MenuCategory = {
  enableIf?: () => boolean,
  children: MenuItem[]
}

type SidebarProps = {
  isOpen: boolean,
  setIsOpen: (value: boolean) => void
}

export default function Sidebar(props: SidebarProps) {
  const router = useRouter();

  const menu: MenuCategory[] = [
    {
      children: [
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
        }
      ]
    },
    {
      children: [
        {
          name: "Користувачі",
          link: "/user",
          icon: UserIcon
        },
        {
          name: "Додаткові запити",
          link: "/extra-query",
          icon: ExtraQueryIcon
        }
      ]
    }
  ];

  const menuEnabled = menu
    .filter(category => category.enableIf?.() ?? true)
    .map(category => {
      const children = category.children.filter(item => item.enableIf?.() ?? true);

      return {...category, children};
    });
  const maxCategorySize = Math.max(...menuEnabled.map(category => category.children.length));

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
        {
          menuEnabled.flatMap((category, categoryIndex) => {
            const entries = category.children.map((item, index) => (
              <ListItem key={categoryIndex * maxCategorySize + index} disablePadding>
                <ListItemButton onClick={() => router.push(item.link)}>
                  <ListItemIcon>
                    {item.icon()}
                  </ListItemIcon>
                  <ListItemText primary={item.name} />
                </ListItemButton>
              </ListItem>
            ));

            if (categoryIndex != menuEnabled.length - 1)
              entries.push(<Divider />);

            return entries;
          })
        }
      </List>
    </Drawer>
  );
}
