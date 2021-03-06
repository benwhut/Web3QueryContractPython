# Web3QueryContractPython
Example of how to dynamically query read/write functions for a given Smart Contract using just the contract address (no ABI necessary) using Web3 in Python. Will dynamically retrieve the contract's ABI through etherscan's API.  

1. Create Python virtual environment (optional)  
`python -m venv venv`  
`source venv/bin/activate`

2. Install web3.py  
`pip install web3`

3. Add your Ethereum endpoint URL using Infura or equivalent  
This is required to query the Ethereum blockchain  
`infura_url = "https://mainnet.infura.io/v3/00000000000000000000000"`

4. Add the address of the Smart Contract you want to query  
You can get this from etherscan.io  
`address = web3.toChecksumAddress("0x00000000000000000000000")`

5. run web3QueryContract.py  
`python3 web3QueryContract.py`  


Output should be similar to this:  

```
READ CONTRACT FUNCTIONS:
contractURI: https://nft.syn.city/meta/SYNP/
maxTokenId: 888
name: Syn City Genesis Passes
nextTokenId: 409
owner: 0x41BDD852d3618Dc5D6338279F373Bf7935dc0242
symbol: SYNP
tokenURIHasBeenFrozen: False
validator: 0xc626be886d4b7D09898152c61959A9a898a78D6f

WRITE CONTRACT FUNCTIONS
approve
claimFreeToken
encodeForSignature
freezeBaseTokenURI
giveawayToken
renounceOwnership
revokeOperator
safeTransferFrom
safeTransferFrom
setApprovalForAll
setOperators
setValidator
transferFrom
transferOwnership
updateBaseTokenURI
```

There are also some examples of how to call individual functions directly using Web3's call() function (commented out by default).

Questions?  
benwhut@gmail.com
