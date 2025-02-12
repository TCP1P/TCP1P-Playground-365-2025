> note: ta copy dikit dari chat nda ngaruh hehe (dimas)

Solve nya tuh harus samain value dari random integer yang digenerate function `___x_x__x_()`, jadi cara simpelnya tuh bisa langsung call function tersebut, nanti valuenya di masukin ke variabel atau gimana, baru deh call function `x__x_xx__` buat validasi
Ini script dari peserta kemaren yang sempat nanya di dm ku
```
from web3 import Web3
from solcx import compile_files

# Connect to Ethereum node
web3 = Web3(Web3.HTTPProvider("$RPC_URL"))
account_address = "$ACCOUNT_ADDR"
private_key = "$PRIV_KEY"
contract_address = "$CA"

# Check connection
if not web3.is_connected():
    raise Exception("Failed to connect to the Ethereum node")

compiled_abi = compile_files(["./Setup.sol"],
        output_values=["abi"],
        solc_version="0.8.0")

compiled_abi2 = compile_files(["./exp.sol"],
        output_values=["abi"],
        solc_version="0.8.0")

abi = compiled_abi["./Cursed.sol:Cursed"]["abi"]
abi2 = compiled_abi["./Setup.sol:Setup"]["abi"]

# Initialize contract
contract = web3.eth.contract(address=contract_address, abi=abi)
contract2 = web3.eth.contract(address=contract_address, abi=abi2)

# Create attack contract
cursed_addr = contract2.functions.cursed().call()
attack_contract = web3.eth.contract(address=cursed_addr, abi=abi)
call_guess = attack_contract.functions.___x_x__x_().call()
attack = attack_contract.functions.x__x_xx__(call_guess).transact()
print(call_guess)
print(contract2.functions.isSolved().call())
```
Nah penjelasannya kenapa tinggal call function `___x_x__x_()`, itu soalnya enkripsi yang didalemnya itu ada miskalkulasi, jadi dia ga bener2 ngerandom integer, tapi cuman gibberish type-casting aja, meskipun di-deploy dan digenerate berkali-kali valuenya tetep static, yaitu **250864995**

Tapi disini aku pake cara manual gapake script jadinya, tapi ya agak nguli wkwk
Jadi itu function `___x_x__x_()` bisa di copas aja terus compile & deploy di remix ide, nanti bakal ketauan valuenya tuh berapa, nah buat validasinya karena perlu function `x__x_xx__()` yang dimana ada di contract `Cursed.sol`, harus compute contract addressnya dulu, karena yang di provide ke peserta cuman contract address dari `Setup.sol` aja, pake script ini
```
function getContractAddress(address creator_account) public pure returns (address) {
        return address(uint160(uint256(keccak256(abi.encodePacked(bytes1(0xd6), bytes1(0x94), creator_account, bytes1(0x01))))));
    }
```
Tinggal compile & deploy di remix ide lagi sama nanti inputnya pake contract address yang berhasil digenerate tadi, nanti bakal dapet contract address dari function `x__x_xx__()` terus call function nya & input value yg didapetin pake foundry, udah deh dpt flagnya
