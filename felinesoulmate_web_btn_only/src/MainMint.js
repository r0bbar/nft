import { useState} from 'react';
import {Box, Button, Input, Flex, Image, Link, Spacer } from '@chakra-ui/react'
import { ethers, BigNumber } from 'ethers';
import felineSoulmate from './FelineSoulmate.json';
import {Buffer} from 'buffer';

const felineSoulmateAddress = "0x7ca77fb6c0a5b2446A3304a1528E873a4b858251";

const MainMint = ( { accounts, setAccounts } ) => {
    const [ mintAmount, setMintAmount] = useState(1);
    const isConnected = Boolean(accounts[0]);

    async function handlePrivateMint() {
        if (window.ethereum) {
            const { MerkleTree } = require('merkletreejs');
            const keccak256 = require('keccak256');

            let teststr = process.env.REACT_APP_TESTSTR;
            console.log('teststr.length:', teststr.length);
            
            // Hardcoded here! If address not here, "getHexProof" will return null!!
            let whitelistAddresses = process.env.REACT_APP_WHITELIST_ADDRESSES.split(',');
            
            const leafNodes = whitelistAddresses.map(addr => keccak256(addr));
            const merkleTree = new MerkleTree(leafNodes, keccak256, { sortPairs: true});
            const rootHash = merkleTree.getRoot();
            const wallet = accounts[0]
            const wallet_hash = keccak256(wallet)
            const hexProof = merkleTree.getHexProof(wallet_hash);
            console.log('merkleTree (Whitelist)', merkleTree.toString());
            console.log("rootHash: ", rootHash);
            console.log("wallet: ", wallet);
            console.log("wallet_hash", wallet_hash.toString())
            console.log("hexProof: ", hexProof.toString());

            console.log("mintAmount: ", mintAmount);
            const provider = new ethers.providers.Web3Provider(window.ethereum);
            const signer = provider.getSigner();
            const contract = new ethers.Contract(
                felineSoulmateAddress,
                felineSoulmate.abi,
                signer
            );

            try {
                const response = await contract.privateMint(
                    hexProof,
                    BigNumber.from(mintAmount), 
                    { 
                        value: ethers.utils.parseEther(
                                (0.02 * mintAmount).toString()
                            )
                    }
                );
                console.log("Response: ", response);
            } catch(err) {
                console.log("Error", err)
            }
        }
    }

    async function handlePublicMint() {
        if (window.ethereum) {
            console.log("wallet: ", accounts[0]);

            console.log("mintAmount: ", mintAmount);
            const provider = new ethers.providers.Web3Provider(window.ethereum);
            const signer = provider.getSigner();
            const contract = new ethers.Contract(
                felineSoulmateAddress,
                felineSoulmate.abi,
                signer
            );

            try {
                const response = await contract.mint(
                    BigNumber.from(mintAmount), 
                    { 
                        value: ethers.utils.parseEther(
                                (0.02 * mintAmount).toString()
                            )
                    }
                );
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
            {isConnected? (
                <div>
                    <div>
                        <Button 
                            backgroundColor="#212F3C"
                            borderRadius="5px"
                            color="white"
                            cursor="pointer"
                            fontFamily="Arial"
                            padding="15px"
                            margin="0 15px"
                            onClick={handleDecrement}>
                                -
                        </Button>
                        <Input 
                            readOnly
                            fontFamily="Arial"
                            width="100px"
                            height="40px"
                            textAlign="center"
                            paddingLeft="19px"
                            marginTop="10px"
                            type="number"
                            value={mintAmount} />
                        <Button 
                            backgroundColor="#212F3C" 
                            borderRadius="5px"
                            color="white"
                            cursor="pointer"
                            fontFamily="Arial"
                            padding="15px"
                            margin="0 15px"
                            onClick={handleIncrement}>
                                +
                        </Button>
                    </div>
                    <br></br>
                    {process.env.REACT_APP_ENABLE_PUBLIC_MINT=='true'? (
                        <Button 
                            backgroundColor="#212F3C" 
                            borderRadius="25px"
                            color="white"
                            cursor="pointer"
                            fontFamily="inherit"
                            padding="15px"
                            margin="0 15px"
                            width="200px"
                            onClick={handlePublicMint}>
                                Mint Now!
                        </Button>
                    ) : (
                        <Button 
                            backgroundColor="#212F3C" 
                            borderRadius="25px"
                            color="white"
                            cursor="pointer"
                            fontFamily="inherit"
                            padding="15px"
                            margin="0 15px"
                            width="200px"
                            onClick={handlePrivateMint}>
                                Private Mint, VIP only.
                        </Button>
                    )}
                </div>
            ) : (
                <p>You must be connected to Mint.</p>
            )
            }
        </div>

    );
}

export default MainMint;