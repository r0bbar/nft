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

To verify:
    npx hardhat verify --network rinkeby $ADDRESS$

Check hash via https://rinkeby.etherscan.io/

7. Copy "FelineSoulmate.json"
    FROM: C:\dev\nft\felinesoulmate_web\artifacts\contracts
    TO: C:\dev\nft\felinesoulmate_web\src

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



