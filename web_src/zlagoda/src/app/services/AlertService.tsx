import React, { createContext, useContext, useState } from 'react';
import Snackbar from '@mui/material/Snackbar';
import {Alert, AlertColor} from "@mui/material";

function alertProviderMissing(message: string, severity: AlertColor) {
    throw new Error("AlertProvider is missing");
}

export const AlertContext = createContext(alertProviderMissing);

export const AlertProvider = ({ children }: { children: React.ReactNode }) => {
    const [isOpen, setIsOpen] = useState(false);
    const [message, setMessage] = useState("");
    const [severity, setSeverity] = useState<AlertColor>("info");

    const showAlert = (newMessage: string, newSeverity: AlertColor = "info") => {
        setMessage(newMessage);
        setSeverity(newSeverity);
        setIsOpen(true);
    };

    const hideAlert = () => {
        setIsOpen(false);
    };

    // TODO: Create multiple snackbars
    return (
        <AlertContext.Provider value={showAlert}>
            {children}
            <Snackbar
                open={isOpen}
                autoHideDuration={3000}
                onClose={hideAlert}
                anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
            >
                <Alert
                    onClose={hideAlert}
                    severity={severity}
                    variant="filled"
                    sx={{ width: '100%' }}
                >
                    {message}
                </Alert>
            </Snackbar>
        </AlertContext.Provider>
    );
};
