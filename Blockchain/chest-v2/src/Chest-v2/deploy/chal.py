import json
from pathlib import Path

import eth_sandbox
from web3 import Web3


def deploy(
    web3: Web3, deployer_address: str, deployer_privateKey: str, player_address: str
) -> str:
    contract_info = json.loads(Path("compiled/Setup.sol/Setup.json").read_text())

    abi = contract_info["abi"]
    bytecode = contract_info["bytecode"]["object"]

    contract = web3.eth.contract(abi=abi, bytecode=bytecode)

    combinations = [
        0xF4D58EB6603CA01695B2A17F0F97CA9946CA2918F16FD7BDE991A1719D3A38F0,
        0xC7BEEE321B17BD42B03C3B9B1D10DF0FFE692146ED8CFD2092A44460AE61D660,
    ]
    golden_key = 0x0814C57347C9F214E8DA678763ECD791C29CD09A7C308EC91FDFCF5AD0ECEC3D

    construct_txn = contract.constructor(combinations, golden_key).build_transaction(
        {
            "from": deployer_address,
            "nonce": web3.eth.get_transaction_count(deployer_address),
        }
    )

    tx_create = web3.eth.account.sign_transaction(construct_txn, deployer_privateKey)
    tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)

    rcpt = web3.eth.wait_for_transaction_receipt(tx_hash)

    return rcpt.contractAddress


app = eth_sandbox.run_launcher(deploy)
