import json
import asyncio
from web3 import Web3
import json
from datetime import datetime


my_wallet_address = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
wallet_address = Web3.toChecksumAddress(my_wallet_address)
private_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


'''
https://rinkeby.etherscan.io/address/0x3b89C321e7B4a00E13f8c239BeF72A454219AeAb
'''
infura_rinkeby_rpc = "https://rinkeby.infura.io/v3/cbbff76dc51e42e5af018b6e7059be68"
w3 = Web3(Web3.HTTPProvider(infura_rinkeby_rpc))

ONE_BILLION : int = 1000000000
default_gas_limit = 800_000
gas_price = w3.eth.gasPrice
chain_id = w3.eth.chainId

nft_contract_address = Web3.toChecksumAddress("0x37032A51Ba0bF51E51086a68BF8C643D5776aF90")
nft_contract_abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"ApprovalCallerNotOwnerNorApproved","type":"error"},{"inputs":[],"name":"ApprovalQueryForNonexistentToken","type":"error"},{"inputs":[],"name":"ApprovalToCurrentOwner","type":"error"},{"inputs":[],"name":"ApproveToCaller","type":"error"},{"inputs":[],"name":"BalanceQueryForZeroAddress","type":"error"},{"inputs":[],"name":"MintToZeroAddress","type":"error"},{"inputs":[],"name":"MintZeroQuantity","type":"error"},{"inputs":[],"name":"OwnerIndexOutOfBounds","type":"error"},{"inputs":[],"name":"OwnerQueryForNonexistentToken","type":"error"},{"inputs":[],"name":"TokenIndexOutOfBounds","type":"error"},{"inputs":[],"name":"TransferCallerNotOwnerNorApproved","type":"error"},{"inputs":[],"name":"TransferFromIncorrectOwner","type":"error"},{"inputs":[],"name":"TransferToNonERC721ReceiverImplementer","type":"error"},{"inputs":[],"name":"TransferToZeroAddress","type":"error"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"totalMinted","type":"uint256"}],"name":"Minted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"_transferToContract","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"addressMintedBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"allowedToContract","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_newPrice","type":"uint256"}],"name":"changePrice","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isPrivateMintEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isPublicMintEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isRevealed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxMintPerTx","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxMintPerWallet","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_count","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"price","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32[]","name":"_merkleProof","type":"bytes32[]"},{"internalType":"uint256","name":"_count","type":"uint256"}],"name":"privateMint","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"privateMintMerkleRoot","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"privateMintParticipants","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"setAllowToContract","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"},{"internalType":"bool","name":"_allow","type":"bool"}],"name":"setAllowTokenToContract","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_hiddenMetadataUri","type":"string"}],"name":"setHiddenMetadataUri","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"isPrivateMintEnabled_","type":"bool"}],"name":"setIsPrivateMintEnabled","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"isPublicMintEnabled_","type":"bool"}],"name":"setIsPublicMintEnabled","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_state","type":"bool"}],"name":"setIsRevealed","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_maxMintPerTx","type":"uint256"}],"name":"setMaxMintPerTx","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_maxMintPerWallet","type":"uint256"}],"name":"setMaxMintPerWallet","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_privateMintMerkleRoot","type":"bytes32"}],"name":"setPrivateMintMerkleRoot","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_uriPrefix","type":"string"}],"name":"setUriPrefix","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_uriSuffix","type":"string"}],"name":"setUriSuffix","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"withdrawWalletAddress_","type":"address"}],"name":"setWithdrawWallet","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"tos","type":"address[]"}],"name":"teamMint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"uriSuffix","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"walletOfOwner","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdrawWallet","outputs":[{"internalType":"address payable","name":"","type":"address"}],"stateMutability":"view","type":"function"}]' 
nft_contract_abi = json.loads(nft_contract_abi)
i : int = 0
for entry in nft_contract_abi:
    if 'name' not in entry:
        entry['name'] = f"dummy_name_{i}"
        i = i+1
nft_contract = w3.eth.contract(address=nft_contract_address, abi=nft_contract_abi)


try:
    merkle_root = "9875131d8853b4cdcd0dc3f73457b0956852bd604929745ea0ef80d7aec13a1c"

    deadline = int(datetime.now().timestamp() + 180)  # 3 mn for this example
    function_params = nft_contract.functions.setPrivateMintMerkleRoot(merkle_root)
    nonce = w3.eth.getTransactionCount(wallet_address)
    trx_params = function_params.buildTransaction(
        {
            'from': wallet_address,
            'gas': default_gas_limit,
            'gasPrice': gas_price,
            'nonce': nonce,
            'chainId': chain_id,
            'value': 0,
        }
    )

    signed = w3.eth.account.sign_transaction(trx_params, private_key)
    trx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
    print(f"trx_hash: {trx_hash.hex()}")
    
except Exception as error:
    print(f"{error}")


try:

    owner = nft_contract.functions.owner().call()

    # https://coinguides.org/ethereum-unit-converter-gwei-ether/
    mintPrice = nft_contract.functions.price().call()
    mintPrice = mintPrice / (ONE_BILLION * ONE_BILLION)

    print(f"Owner wallet is: {owner}, mintPrice: {mintPrice}")
except Exception as error:
    print(f"{error}")

try:
    deadline = int(datetime.now().timestamp() + 180)  # 3 mn for this example
    function_params = nft_contract.functions.setIsPrivateMintEnabled(True)
    nonce = w3.eth.getTransactionCount(wallet_address)
    trx_params = function_params.buildTransaction(
        {
            'from': wallet_address,
            'gas': default_gas_limit,
            'gasPrice': gas_price,
            'nonce': nonce,
            'chainId': chain_id,
            'value': 0,
        }
    )

    signed = w3.eth.account.sign_transaction(trx_params, private_key)
    trx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
    print(f"trx_hash: {trx_hash.hex()}")

    is_private_mint_enabled = False
    while not is_private_mint_enabled:
        is_private_mint_enabled = nft_contract.functions.isPrivateMintEnabled().call()
    assert(is_private_mint_enabled)

    print(f"is_private_mint_enabled: {is_private_mint_enabled}")
except Exception as error:
    print(f"{error}")

try:
    deadline = int(datetime.now().timestamp() + 180)  # 3 mn for this example
    function_params = nft_contract.functions.setIsPublicMintEnabled(True)
    nonce = w3.eth.getTransactionCount(wallet_address)
    trx_params = function_params.buildTransaction(
        {
            'from': wallet_address,
            'gas': default_gas_limit,
            'gasPrice': gas_price,
            'nonce': nonce,
            'chainId': chain_id,
            'value': 0,
        }
    )

    signed = w3.eth.account.sign_transaction(trx_params, private_key)
    trx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
    print(f"trx_hash: {trx_hash.hex()}")

    is_public_mint_enabled = False
    while not is_public_mint_enabled:
        is_public_mint_enabled = nft_contract.functions.isPublicMintEnabled().call()
    assert(is_public_mint_enabled)

    print(f"is_public_mint_enabled: {is_public_mint_enabled}")
except Exception as error:
    print(f"{error}")

