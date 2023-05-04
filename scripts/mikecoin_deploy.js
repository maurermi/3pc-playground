async function main() {
    const [deployer] = await ethers.getSigners();

    console.log("Deploying contracts with the account:", deployer.address);

    const weiAmount = (await deployer.getBalance()).toString();

    console.log("Account balance:", (await ethers.utils.formatEther(weiAmount)));

    const Token = await ethers.getContractFactory("MikeCoin");
    const token = await Token.deploy();

    console.log("Token address:", token.address);
    console.log("transaction:", token.deployTransaction);
    const waiting = await token.deployTransaction.wait();
    console.log("waiting:", waiting);
    //await token.value();
  }

  main()
    .then(() => process.exit(0))
    .catch((error) => {
      console.error(error);
      process.exit(1);
  });