const main = async () => {
    const USDStableFactory = await hre.ethers.getContractFactory("USDStable");
    const USDStable = await USDStableFactory.deploy();

    await USDStable.deployed();

    const ShippingAgreementFactory = await hre.ethers.getContractFactory("ShippingAgreement");
    const shippingAgreement = await ShippingAgreementFactory.deploy({
        value: hre.ethers.utils.parseEther("0.001"),
    });

    await shippingAgreement.deployed();

    console.log("WavePortal address: ", shippingAgreement.address);
};

const runMain = async () => {
    try {
        await main();
        process.exit(0);
    } catch (error) {
        console.error(error);
        process.exit(1);
    }
};

runMain();