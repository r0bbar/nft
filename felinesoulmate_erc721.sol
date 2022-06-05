// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.4;

import '@openzeppelin/contracts/token/ERC721/ERC721.sol';
import '@openzeppelin/contracts/access/Ownable.sol';
import '@openzeppelin/contracts/utils/cryptography/MerkleProof.sol';

error ExceedMaxSupply();

contract FelineSoulmate is ERC721, Ownable {
    uint256 public mintPrice;
    uint256 public totalSupply;
    uint256 public maxSupply;
    uint256 public maxPerWallet;
    bool public isPrivateMintEnabled;
    bool public isPublicMintEnabled;
    string internal baseTokenUri;
    address payable public withdrawWallet;
    mapping(address => uint256) public walletMints;

    bytes32 public privateMintMerkleRoot;

    mapping(address => bool) public privateMintParticipants;

    constructor () payable ERC721('FelineSoulmate', 'FS') {
        mintPrice = 0.02 ether;
        totalSupply = 0;
        maxSupply = 5000;
        maxPerWallet = 3;

        withdrawWallet = payable(msg.sender);
    }

    function setWithdrawWallet(address withdrawWalletAddress_) external onlyOwner {
        withdrawWallet = payable(withdrawWalletAddress_);
    }

    function setMintPrice(uint256 _mintPrice) public onlyOwner {
        mintPrice = _mintPrice;
    }

    function setMaxSupply(uint256 _maxSupply) public onlyOwner {
        maxSupply = _maxSupply;
    }

    function setMaxPerWallet(uint256 _maxPerWallet) public onlyOwner {
        maxPerWallet = _maxPerWallet;
    }

    function setPrivateMintMerkleRoot(bytes32 _privateMintMerkleRoot) external onlyOwner {
        privateMintMerkleRoot = _privateMintMerkleRoot;
    }

    function setIsPrivateMintEnabled(bool isPrivateMintEnabled_) external onlyOwner {
        isPrivateMintEnabled = isPrivateMintEnabled_;
    }

    function setIsPublicMintEnabled(bool isPublicMintEnabled_) external onlyOwner {
        isPublicMintEnabled = isPublicMintEnabled_;
    }

    function setBaseTokenUri(string calldata baseTokenUri_) external onlyOwner {
        baseTokenUri = baseTokenUri_;
    }

    function tokenURI(uint256 tokenId_) public view override returns (string memory) {
        require(_exists(tokenId_), 'Token does not exist!');
        return string(abi.encodePacked(baseTokenUri, Strings.toString(tokenId_), ".json"));
    }

    function withdraw() external onlyOwner {
        (bool success, ) = withdrawWallet.call{ value: address(this).balance }('');
        require(success, 'withdraw failed');
    }

    function teamMint(address[] memory tos) external onlyOwner {
        for (uint256 i = 0; i < tos.length; i++) {
            uint256 newTokenId = totalSupply + 1;
            totalSupply ++;
            _safeMint(tos[i], newTokenId);

            walletMints[tos[i]] = walletMints[tos[i]] + 1;
        }
        totalSupply += tos.length;

        if (totalSupply > maxSupply) { revert ExceedMaxSupply(); }
    }

    function privateMint(bytes32[] calldata _merkleProof, uint256 quantity_) external payable {
        require(isPrivateMintEnabled, 'Private Minting not enabled.');
        require(tx.origin == msg.sender, 'Contract Denied.'); // https://ethereum.stackexchange.com/questions/113962/what-does-msg-sender-tx-origin-actually-do-why
        require(msg.value == quantity_ * mintPrice, 'Invalid mint value.');
        require(totalSupply + quantity_ <= maxSupply, 'Sold out!');
        require(walletMints[msg.sender] + quantity_ <= maxPerWallet, 'Exceed max wallet!');
        require(!privateMintParticipants[msg.sender], 'Mint already claimed!');

        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        require(MerkleProof.verify(_merkleProof, privateMintMerkleRoot, leaf), 'Proof Invalid');

        for(uint256 i = 0; i < quantity_; i++) {
            uint256 newTokenId = totalSupply + 1;
            totalSupply ++;
            _safeMint(msg.sender, newTokenId);
        }

        walletMints[msg.sender] = walletMints[msg.sender] + quantity_;
        privateMintParticipants[msg.sender] = true;
    }

    function mint(uint256 quantity_) public payable {
        require(isPublicMintEnabled, 'Public Minting not enabled.');
        require(tx.origin == msg.sender, 'Contract Denied.'); // https://ethereum.stackexchange.com/questions/113962/what-does-msg-sender-tx-origin-actually-do-why
        require(msg.value == quantity_ * mintPrice, 'Invalid mint value.');
        require(totalSupply + quantity_ <= maxSupply, 'Sold out!');
        require(walletMints[msg.sender] + quantity_ <= maxPerWallet, 'Exceed max wallet!');

        for(uint256 i = 0; i < quantity_; i++) {
            uint256 newTokenId = totalSupply + 1;
            totalSupply ++;
            _safeMint(msg.sender, newTokenId);
        }

        walletMints[msg.sender] = walletMints[msg.sender] + quantity_;
    }
}