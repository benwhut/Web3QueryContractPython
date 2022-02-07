# QuerySmartContractFunctions
Dynamically query read/write functions for a given Smart Contract using Web3 in Python

1. Create virtual environment (optional)
python -m venv venv

2. Install web3.py
pip install web3

3. Add your Ethereum blockchain endpoint using Infura or equivalent
infura_url = "https://mainnet.infura.io/v3/..."

4. Add the address of the Smart Contract you want to query
address = web3.toChecksumAddress("0x6...")

5. run queryFunc.py
python3 queryFunc.py



