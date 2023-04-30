const ValidatorRatings = artifacts.require("ValidatorRatings");

module.exports = function(deployer) {
  deployer.deploy(ValidatorRatings);
};
