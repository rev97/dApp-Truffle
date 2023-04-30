# dApp - Validating ML models in a decentralized way
Created to implement decentralized ML in Ganache testnets using Truffle

We have implemented our setup design by using Truffle - Ganache -Remix Suite where smart contracts are developed in solidity. Smart contract that is developed is compiled using truffle and deployed in ganache local servers. Users can acccess the data and methods in the deployed contract using remix ide where ganache testnets are accessed using the http web sockets.

To implement this setup one needs to have the following items installed in thier local machine

* Ganache Application
* Truffle 
* Web3 python package
* Solidity compiler >=0.6.0 <0.9.0

# Truffle Setup

* git clone this repository using 'git clone https://github.com/rev97/dApp-Truffle.git'
* Now install truffle in local machine using 'npm install g-truffle' command
* Go to the cloned repo and compile the solidity contract that is present in contracts folder using 'truffle compile' command

# Ganache Setup

* Go to this page https://trufflesuite.com/ganache/ and download ganache application depending on your operating system
* Login to the ganache application and create a truffle project by adding the path of truffle_config.js file in this repository while adding the project.
* Please make sure that the port in which ganache network is being launched. For local host the default ip address is "127.0.0.1" and port is "9545". We can find these details in config file.
* If the ganache server is running on different port then enter that port value in config file.

# Deploy Contract

* Once the ganache server starts running, deploy the compiled contract using 'truffle migrate' command which starts a blockchain transaction and creates a genesis block at first.

# Remix IDE

* To access the data and methods in the solidity code, Create an account in remix IDE, now copy the solidity file present in this repository and paste it in the contracts folder
* Now compile the solidity code and while deploying provide the http web socket address of the ganache chain in which contract is previously deployed and also provide the contract address of the ganache block in which sol code is deployed.
* Now we can see that using remix we can access our local blockchain that is hosted in the ganache server.

# Web3 Python 

* For performing off chain operations, we first need to make sure that python3 is installed in your local machine and latest version of pip is available.
* Now install web3 package using 'pip3 install web3' command.
* There are three python scripts (integrate.py, setRatings, write_tx)in this repo, which interacts with the ethereum blockchains that are hosted in ganache servers.
* integrate.py - reads the methods from the contracts.
* write_tx.py - reads the data and writes the new transactions into the chain.
* setRatings.py - analysis the data and updates the values of variables in the chain.