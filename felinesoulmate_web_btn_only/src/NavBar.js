import React from 'react';
import {Box, Button, Flex } from '@chakra-ui/react'

const NavBar = ({ accounts, setAccounts} ) => {
    const isConnected = Boolean(accounts[0]);

    async function connectAccount() {
        if(window.ethereum) {
            const accounts = await window.ethereum.request({
                method : "eth_requestAccounts",
            });
            setAccounts(accounts);
        }
    }

    return (
        <Flex padding="30px" justifyContent="center">
            { /* Connect */ }
            { isConnected ? (
                <Box>Connected</Box>
            ) : (
                <Button 
                    backgroundColor="#212F3C" 
                    borderRadius="25px"
                    color="white"
                    cursor="pointer"
                    fontFamily="inherit"
                    padding="15px"
                    width="200px"
                    margin="0 15px"
                    onClick={connectAccount}>
                        Connect
                </Button>
            )}
        </Flex>
    )
}

export default NavBar;