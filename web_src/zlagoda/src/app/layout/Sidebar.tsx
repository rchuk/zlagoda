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
import {useRouter} from "next/router";
import {SIDEBAR_WIDTH} from "@/app/components/common/utils/Constants";
import {Navigation, NavigationItem} from "@/app/layout/Navigation";
import {useEffect, useState} from "react";


const DrawerHeader = styled('div')(({ theme }) => ({
  display: 'flex',
  alignItems: 'center',
  padding: theme.spacing(0, 1),
  ...theme.mixins.toolbar,
  justifyContent: 'flex-end'
}));

type MenuCategory = {
  isEnabled?: () => boolean,
  children: NavigationItem[]
}

type SidebarProps = {
  isOpen: boolean,
  setIsOpen: (value: boolean) => void
}

export default function Sidebar(props: SidebarProps) {
  const [menuEnabled, setMenuEnabled] = useState<MenuCategory[]>([]);
  const router = useRouter();

  const menu: MenuCategory[] = [
    {
      children: [
        Navigation.customerCard,
        Navigation.receipt,
        Navigation.product,
        Navigation.productArchetype,
        Navigation.productCategory,
        Navigation.employee
      ]
    },
    {
      children: [
        Navigation.users,
        Navigation.extraQuery
      ]
    }
  ];

  /*
  const menuEnabled = menu
    .filter(category => category.isEnabled?.() ?? true)
    .map(category => {
      const children = category.children.filter(item => item.isEnabled?.() ?? true);

      return {...category, children};
    });
   */
  useEffect(() => {
    const newMenuEnabled = menu
      .filter(category => category.isEnabled?.() ?? true)
      .map(category => {
        const children = category.children.filter(item => item.isEnabled?.() ?? true);

        return {...category, children};
      });

    setMenuEnabled(newMenuEnabled);
  }, []);

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
          <ChevronLeftIcon color="primary" />
        </IconButton>
      </DrawerHeader>
      <List>
        {
          menuEnabled.flatMap((category, categoryIndex) => {
            const entries = category.children.map((item, index) => (
              <ListItem key={item.path} disablePadding>
                <ListItemButton onClick={() => router.push(item.path)}>
                  <ListItemIcon>
                    {item.icon()}
                  </ListItemIcon>
                  <ListItemText primary={item.title} />
                </ListItemButton>
              </ListItem>
            ));

            if (categoryIndex != menuEnabled.length - 1)
              entries.push(<Divider key={categoryIndex}/>);

            return entries;
          })
        }
      </List>
    </Drawer>
  );
}
