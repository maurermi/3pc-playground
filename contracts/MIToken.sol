// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MIToken is ERC20 {
    constructor() ERC20("MIToken", "MIT") {
        _mint(msg.sender, 50000000 * (10 ** 18));
    }

    function requestTokens(address requestor) public {
        _mint(requestor, 1 * (10 ** 18));
    }
}
