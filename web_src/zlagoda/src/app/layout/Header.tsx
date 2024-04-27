import {Box, Button, IconButton, MenuItem, styled, Toolbar} from "@mui/material";
import MuiAppBar, { AppBarProps as MuiAppBarProps } from '@mui/material/AppBar';
import React, {useContext, useState} from "react";
import {FullscreenServiceContext} from "@/app/services/FullscreenService";
import MenuIcon from '@mui/icons-material/Menu';
import FullscreenIcon from '@mui/icons-material/Fullscreen';
import FullscreenExitIcon from '@mui/icons-material/FullscreenExit';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import Image from "next/image";
import {SIDEBAR_WIDTH} from "@/app/components/common/utils/Constants";
import {useRouter} from "next/router";
import {Menu} from "@mui/material";
import {AuthServiceContext} from "@/app/services/AuthService";

interface AppBarProps extends MuiAppBarProps {
  isSidebarOpen: boolean
}

const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== 'isSidebarOpen',
})<AppBarProps>(({ theme, isSidebarOpen }) => ({
  transition: theme.transitions.create(['margin', 'width'], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  ...(isSidebarOpen && {
    width: `calc(100% - ${SIDEBAR_WIDTH}px)`,
    marginLeft: `${SIDEBAR_WIDTH}px`,
    transition: theme.transitions.create(['margin', 'width'], {
      easing: theme.transitions.easing.easeOut,
      duration: theme.transitions.duration.enteringScreen,
    }),
  }),
}));

type HeaderProps = {
  isSidebarOpen: boolean,
  setIsSidebarOpen: (value: boolean) => void
}

export default function Header(props: HeaderProps) {
  const [anchorEl, setAnchorEl] = useState<HTMLElement | null>(null);
  const isAccountOpen = Boolean(anchorEl);
  const authService = useContext(AuthServiceContext);

  const fullscreenHandle = useContext(FullscreenServiceContext);
  const router = useRouter();

  function toggleSidebar() {
    props.setIsSidebarOpen(!props.isSidebarOpen);
  }

  function handleLogoClick() {
    router.push("/");
  }

  function handleAccountOpen(event: React.MouseEvent<HTMLElement>) {
    setAnchorEl(event.currentTarget);
  }

  function handleAccountClose() {
    setAnchorEl(null);
  }

  function handleLogout() {
    authService.logout();
    handleAccountClose();
  }

  return (
    <AppBar position="static" isSidebarOpen={props.isSidebarOpen}>
      <Toolbar>
        {
          !props.isSidebarOpen && authService.isLoggedIn() &&
          <IconButton onClick={toggleSidebar} size="large">
            <MenuIcon sx={{ color: theme => theme.palette.almostWhite.main }} />
          </IconButton>
        }
        <Box display="flex" flexGrow={1} justifyContent="center">
          <Button disableRipple onClick={handleLogoClick} sx={{ padding: 0 }}>
            <Image src="zlagoda_logo.svg" width={200} height={80} alt="Злагода" />
          </Button>
        </Box>
        {
          fullscreenHandle.active
            ? (
              <IconButton onClick={fullscreenHandle.exit} size="large">
                <FullscreenExitIcon sx={{ color: theme => theme.palette.almostWhite.main }} />
              </IconButton>
            )
            : (
              <IconButton onClick={fullscreenHandle.enter} size="large">
                <FullscreenIcon sx={{ color: theme => theme.palette.almostWhite.main }} />
              </IconButton>
            )
        }
        {
          authService.isLoggedIn() &&
          <IconButton onClick={handleAccountOpen}>
            <AccountCircleIcon sx={{ color: theme => theme.palette.almostWhite.main }} />
          </IconButton>
        }
        {
          authService.isLoggedIn() &&
          <Menu
            anchorEl={anchorEl}
            open={isAccountOpen}
            onClose={handleAccountClose}
          >
            <MenuItem onClick={handleAccountClose}>Profile</MenuItem>
            <MenuItem onClick={handleLogout}>Logout</MenuItem>
          </Menu>
        }
      </Toolbar>
    </AppBar>
  );
}
