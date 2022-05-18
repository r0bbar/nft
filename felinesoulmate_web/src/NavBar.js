import React from 'react';
import {Box, Button, Flex, Image, Link, Spacer } from '@chakra-ui/react'
import Facebook from "./assets/social-media-icons/facebook_32x32.png"
import Twitter from "./assets/social-media-icons/twitter_32x32.png"
import Discord from "./assets/social-media-icons/discord_32x32.png"

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
        <Flex justify="space-between" align="center" padding="30px">
            { /* Social Media */ }
            <Flex justify="space-around" width="40%" padding="0 75px">
                <Link href="https://www.facebook.com">
                    <Image src={Facebook} bookSize="42px" margin="0 15px" />
                </Link>
                <Link href="https://www.twitter.com">
                    <Image src={Twitter} bookSize="42px" margin="0 15px" />
                </Link>
                <Link href="https://www.discord.com">
                    <Image src={Discord} bookSize="42px" margin="0 15px" />
                </Link>
            </Flex>

            { /* Right side Connect buttons */ }
            <div>About</div>
            <div>Mint</div>
            <div>Team</div>

            { /* Connect */ }
            { isConnected ? (
                <Box>Connected</Box>
            ) : (
                <Button 
                    backgroundColor="#D6517D" 
                    borderRadius="5px"
                    boxShadow="0px 2px 2px 1px #0F0F0F"
                    color="white"
                    cursor="pointer"
                    fontFamily="inherit"
                    padding="15px"
                    margin="0 15px"
                    onClick={connectAccount}>
                        Connect
                </Button>
            )}
        </Flex>
    )
}

export default NavBar;