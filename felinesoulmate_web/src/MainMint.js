import { useState} from 'react';
import {Box, Button, Input, Flex, Image, Link, Spacer } from '@chakra-ui/react'
import { ethers, BigNumber } from 'ethers';
import felineSoulmate from './FelineSoulmate.json';

const felineSoulmateAddress = "";

const MainMint = ( { accounts, setAccounts } ) => {
    const [ mintAmount, setMintAmount] = useState(1);
    const isConnected = Boolean(accounts[0]);

    async function handleMint() {
        if (window.ethereum) {
            const provider = new ethers.providers.Web3Provider(window.ethereum);
            const signer = provider.getSigner();
            const contract = new ethers.Contract(
                felineSoulmateAddress,
                felineSoulmate.abi,
                signer
            );

            try {
                const response = await contract.mint(mintAmount);
                console.log("Response: ", response);
            } catch(err) {
                console.log("Error", err)
            }
        }
    }

    const handleDecrement = () => {
        if (mintAmount <= 1) return ;
        setMintAmount(mintAmount -1);
    }

    const handleIncrement = () => {
        if (mintAmount >=3) return;
        setMintAmount(mintAmount + 1);
    }

    return  (
        <div>
            <h1>Feline Soulmate</h1>
            <p>Blah blah</p>
            {isConnected? (
                <div>
                    <div>
                        <Button 
                            backgroundColor="#D6517D" 
                            borderRadius="5px"
                            boxShadow="0px 2px 2px 1px #0F0F0F"
                            color="white"
                            cursor="pointer"
                            fontFamily="inherit"
                            padding="15px"
                            margin="0 15px"
                            onClick={handleDecrement}>
                                -
                        </Button>
                        <Input 
                            readOnly
                            fontFamily="inherit"
                            width="100p"
                            height="40px"
                            textAlign="center"
                            paddingLeft="19px"
                            marginTop="10px"
                            type="number"
                            value={mintAmount} />
                        <Button 
                            backgroundColor="#D6517D" 
                            borderRadius="5px"
                            boxShadow="0px 2px 2px 1px #0F0F0F"
                            color="white"
                            cursor="pointer"
                            fontFamily="inherit"
                            padding="15px"
                            margin="0 15px"
                            onClick={handleIncrement}>
                                +
                        </Button>
                    </div>
                    <Button 
                        backgroundColor="#D6517D" 
                        borderRadius="5px"
                        boxShadow="0px 2px 2px 1px #0F0F0F"
                        color="white"
                        cursor="pointer"
                        fontFamily="inherit"
                        padding="15px"
                        margin="0 15px"
                        onClick={handleMint}>
                            Mint Now!
                    </Button>
                </div>
            ) : (
                <p>You must be connected to Mint.</p>
            )
            }
        </div>

    );
}

export default MainMint;