I. Overall
1. Prepare React website and deploy Smart Contract following steps below in section II
2. Use "Merkle_Tree_Whitelist_NFT-main" to compute merkleRoot
3. Use "nft_contract.py" to set Merkle root to deployed contract
4. Deploy React website to for example https://cloud.digitalocean.com/

For Step 2 and 3, refer to https://docs.google.com/document/d/1PRez5yvBTM_OVmFUaV1fX0Vx6wsTiBUZtPQHGgXwzgo

II. React website preparation
1. Initial install:
    npx create-react-app felinesoulmate_web
    npm i -D hardhat
    npx hardhat
    npm i @openzeppelin/contracts
    npm i -D dotenv
    npm install -D @nomiclabs/hardhat-waffle ethereum-waffle 
    npm i -D @nomiclabs/hardhat-etherscan
    
    https://github.com/chakra-ui/chakra-ui
    npm i @chakra-ui/react @emotion/react@^11 @emotion/styled@^11 framer-motion@^6

2. \ contracts \ felinesoulmate.sol

3. .env 
ATTENTION!!! Format below. Be extremely careful exclude this from git repo (But for deployment to for example Digitalocean, you need include this), as such the repo for production release will contain .env and access to that repo need be restricted to wallet owner (And whoever else absolutely neccessary!!!)

REACT_APP_RINKEBY_RPC_URL='https://rinkeby.infura.io/v3/...' <-- from Infura.io (Make sure you specify correct Network. For testing, "Rinkeby")
REACT_APP_ETHERSCAN_KEY='xxxxxxxxxxxxxxxxxxxxxxxx'  <-- From https://rinkeby.etherscan.io (Testing) or etherscan.io (Production, for real)
REACT_APP_PRIVATE_KEY='xxxxxxxxxxxxxx' <-- Your wallet

This is referenced from "hardhat.config.js".

4. hardhat.config.js - add "networks" (rinkeby) and "etherscan"
require("@nomiclabs/hardhat-waffle");
require("@nomiclabs/hardhat-etherscan");
const dotenv = require("dotenv");
dotenv.config();

module.exports = {
  solidity: "0.8.4",
  networks: {
    rinkeby : {
      url : process.env.REACT_APP_RINKEBY_RPC_URL,
      accounts : [ process.env.REACT_APP_PRIVATE_KEY ],
    }
  },
  etherscan : {
    apiKey : process.env.REACT_APP_ETHERSCAN_KEY,
  },
};

5. Compile contract
    npx hardhat clean
    npx hardhat compile

    PS C:\dev\nft\felinesoulmate> npx hardhat compile
    Downloading compiler 0.8.4
    Compiled 11 Solidity files successfully

6. Deploy contract - will cost you ETH
a. Deploy to Ethereum Mainnet
PS C:\dev\nft\felinesoulmate> npx hardhat run scripts/deployFelinesoulmate.js
FelineSoulmate deployed to: 0x5FbDB2315678afecb367f032d93F642f64180aa3
PS C:\dev\nft\felinesoulmate>

b. Deploy to Rinkeby Testnet
  npx hardhat run scripts/deployFelinesoulmate.js --network rinkeby

Check hash via https://rinkeby.etherscan.io/ or for Rinkeby testnet https://rinkeby.etherscan.io/
At this point you'd notice "Contract" is all gibberish. To fix this, you need hardhat-verify. That's next step.

To verify:
    npx hardhat verify --network rinkeby $ADDRESS$
  
For example,
    (base) xxx:~/dev/nft/nft/felinesoulmate_web_btn_only$ npx hardhat verify --network rinkeby 0x383703e94a2800B35BD97a097a4B6e24D2fb2369
    You are using a version of Node.js that is not supported by Hardhat, and it may work incorrectly, or not work at all.

    Please, make sure you are using a supported version of Node.js.

    To learn more about which versions of Node.js are supported go to https://hardhat.org/nodejs-versions
    Nothing to compile
    Successfully submitted source code for contract
    contracts/felinesoulmate.sol:FelineSoulmate at 0x383703e94a2800B35BD97a097a4B6e24D2fb2369
    for verification on the block explorer. Waiting for verification result...

    Successfully verified contract FelineSoulmate on Etherscan.
    https://rinkeby.etherscan.io/address/0x383703e94a2800B35BD97a097a4B6e24D2fb2369#code

7. ATTENTION!!! Copy "FelineSoulmate.json"
    FROM: C:\dev\nft\felinesoulmate_web\artifacts\contracts
    TO: C:\dev\nft\felinesoulmate_web\src

    And also update contract address in MainMint.js
    (React buttons use this address!!!)

8. React part
    a. App.js
    b. MainMint.js
    c. NavBar.js

    https://onedrive.live.com/?authkey=%21AI94eFqjl4fjeFI&cid=3C186B3EC0DA655D&id=3C186B3EC0DA655D%2130070&parId=3C186B3EC0DA655D%2130067&action=locate 

  To run:
    npm run start


Other references:
    https://faucet.rinkeby.io/
    https://infura.io/
    https://etherscan.io/

    React package.json need downgrade "react-script" from "5.0.1" to "4.0.3". After that, you'd need add "--openssl-legacy-provider". THen after that npm build will fail. You'd need further downgrade "framer-motion"!
    https://stackoverflow.com/questions/70530052/keccak-js-uncaught-referenceerror-buffer-is-not-defined/72371223#72371223

    "dependencies": {
      "@chakra-ui/react": "^2.0.0",
      "@emotion/react": "^11.9.0",
      "@emotion/styled": "^11.8.1",
      "@openzeppelin/contracts": "^4.6.0",
      "@testing-library/jest-dom": "^5.16.4",
      "@testing-library/react": "^13.2.0",
      "@testing-library/user-event": "^13.5.0",
      "Buffer": "^0.0.0",
      "keccak256": "1.0.6",
      "merkletreejs": "0.2.31",
      "react": "^18.1.0",
      "react-dom": "^18.1.0",
      "react-scripts": "4.0.3", <-- 
      "web-vitals": "^2.1.4",
      "framer-motion" : "4.1.7" <-- 
    },
    "scripts": {
      "start": "react-scripts --openssl-legacy-provider start",   <-- 
      "build": "react-scripts --openssl-legacy-provider build",   <-- 
      "test": "react-scripts test",
      "eject": "react-scripts eject"
    },


