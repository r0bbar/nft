const hre = require("hardhat");

async function main() {
  const FelineSoulmate = await hre.ethers.getContractFactory("FelineSoulmate");
  const felineSoulmate = await FelineSoulmate.deploy(); // Solidity constructor no argument!?

  await felineSoulmate.deployed();

  console.log("FelineSoulmate deployed to:", felineSoulmate.address);
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
