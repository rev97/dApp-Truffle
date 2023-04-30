# smart contract
import json
from web3 import Web3, HTTPProvider

def update_transact(account_from,contract,name,rating):

    #Build tx
    new_tx = contract.functions.addmlpeer(name,rating).buildTransaction(
        {
            'from': account_from['address'],
            'nonce': web3.eth.get_transaction_count(account_from['address']),
        }
    )

    # Sign tx with PK
    tx_create = web3.eth.account.sign_transaction(new_tx, account_from['private_key'])

    # Send tx and wait for receipt
    tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    print(f'Tx successful with hash: { tx_receipt.transactionHash.hex() }')


if __name__ =="__main__":

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

    account_from = {
        'private_key': '0x18e1f544a305ce114e725ea47697ec62ea2b3e550ccee6a806a96ee265f02a67',
        'address': '0x36Ef8030c6cDdEAd190A8409C8B3FC7b210B7EcA',
    }
    # load contract info as JSON
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)
        
        # fetch contract's abi - necessary to call its functions
        contract_abi = contract_json['abi']

    #Create contract instance
    validator = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

    #Get current ratings of validators
    ml_peers = validator.functions.retrieve_ml().call()
    sp_reviewers = validator.functions.retrieve_sr().call()
    V_ml,V_sp = 0.7,0.5

    ml_p = dict()
    for i in ml_peers:
        ml_p[i[0]] = [i[0],i[1],0]

    total_sum_ml = 0
    for i in ml_peers:
        sum_ml = V_ml*i[1]/5
        ml_p[i[0]]=[i[0],i[1],sum_ml]
        total_sum_ml+=sum_ml
    total_sum_ml = total_sum_ml/len(ml_peers)

    sp_p = dict()
    for i in sp_reviewers:
        sp_p[i[0]] = [i[0],i[1],0]

    total_sum_spr = 0
    for i in sp_reviewers:
        sum_spr = V_sp*i[1]/5
        sp_p[i[0]]=[i[0],i[1],sum_spr]
        total_sum_spr+=sum_spr

    total_sum_spr = total_sum_spr/len(sp_reviewers)

    total_rating = 0.6*total_sum_ml + 0.4*total_sum_spr
    for key in ml_p.keys():
        if 0< total_rating - ml_p[key][2] and total_rating - ml_p[key][2] <=0.05:
            ml_p[key][1] = ml_p[key][1] + 0.02
            update_transact(account_from,validator,ml_p[key][0],ml_p[key][1])
        elif 0.05 < total_rating - ml_p[key][2] and total_rating - ml_p[key][2]<=0.2:
            ml_p[key][1] = ml_p[key][1]
        elif total_rating - ml_p[key][2]>0.2:
            ml_p[key][1] = ml_p[key][1] - 0.05
            update_transact(account_from,validator,ml_p[key][0],ml_p[key][1])

    for key in sp_p.keys():
        if 0< total_rating - sp_p[key][2] and total_rating - sp_p[key][2] <=0.05:
            sp_p[key][1] = sp_p[key][1] + 0.02
            update_transact(account_from,validator,sp_p[key][0],sp_p[key][1])
        elif 0.05 < total_rating - sp_p[key][2] and total_rating - sp_p[key][2]<=0.2:
            sp_p[key][1] = sp_p[key][1]
        elif total_rating - sp_p[key][2]>0.2:
            sp_p[key][1] = sp_p[key][1] - 0.05
            update_transact(account_from,validator,sp_p[key][0],sp_p[key][1])


