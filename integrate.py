# Python program to call the
# smart contract
import json
from web3 import Web3, HTTPProvider

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:9545'

# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))

web3.eth.defaultAccount = web3.eth.accounts[0]

# Setting the default account (so we don't need
#to set the "from" for every transaction call)

# Path to the compiled contract JSON file
compiled_contract_path = 'build/contracts/ValidatorRatings.json'

# Deployed contract address (see `migrate` command output:
# `contract address`)
deployed_contract_address = '0x328B9bA680a29ced41D64E2fE6B62ff040394881'

# load contract info as JSON
with open(compiled_contract_path) as file:
	contract_json = json.load(file)
	
	# fetch contract's abi - necessary to call its functions
	contract_abi = contract_json['abi']

# Fetching deployed contract reference
contract = web3.eth.contract(
	address = deployed_contract_address, abi = contract_abi)

# Calling contract function (this is not persisted
# to the blockchain)

ret = contract.functions.retrieve_ml().call()

print(ret)
