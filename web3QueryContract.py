#!/usr/bin/python

# Author: Bennett Hui (benwhut@gmail.com)
# GNU General Public License v3.0

import json
import requests
from web3 import Web3

# Dynamically fetch the ABI of the Smart Contract from Etherscan API
def fetch_abi(address):
    ABI_ENDPOINT = 'https://api.etherscan.io/api?module=contract&action=getabi&address='

    response = requests.get('%s%s'%(ABI_ENDPOINT, address))
    response_json = response.json()
    abi_json = json.loads(response_json['result'])
    result = json.dumps(abi_json)
    
    return result

def __main__():
    # Enter your own Ethereum blockchain endpoint (Infura or equivalent)
    infura_url = "https://mainnet.infura.io/v3/00000000000000000000000"
    web3 = Web3(Web3.HTTPProvider(infura_url))

    # Enter address of the Smart Contract
    address = web3.toChecksumAddress("0x00000000000000000000000")
    abi = fetch_abi(address)
    contract = web3.eth.contract(address=address, abi=abi)

    abi_output = json.loads(abi)
    array_length = len(abi_output)

    print("\nREAD CONTRACT FUNCTIONS:")
    for i in range(array_length):
        # Query all Read Functions with their values
        if "type" in abi_output[i] and abi_output[i]["type"] == "function" and not abi_output[i]["inputs"]:
            if abi_output[i]["stateMutability"] == "view":
                # Get the funciton name
                func_name = abi_output[i]["name"]
                # Call function and get the value
                func_value = eval("contract.functions." + func_name + "().call()")
                print(func_name + ": " + str(func_value))

    print("\nWRITE CONTRACT FUNCTIONS")
    for i in range(array_length):
        # Query all Write Functions
        if "type" in abi_output[i] and abi_output[i]["type"] == "function":
            if abi_output[i]["stateMutability"] != "view":
                print(abi_output[i]["name"])

    # Call individual functions and print them
    #name = contract.functions.name().call()
    #symbol = contract.functions.symbol().call()
    #price = web3.fromWei(contract.functions.PRICE().call(), "ether")
    #baseTokenURI = contract.functions.baseTokenURI().call()

    #print("Name:", name)
    #print("Symbol:", symbol)
    #print("Price (ETH):", price)
    #print("baseTokenURI:", baseTokenURI)


if __name__ == '__main__':
    __main__()
