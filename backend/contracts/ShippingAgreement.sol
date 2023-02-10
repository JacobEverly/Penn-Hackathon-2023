// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.9;

// Uncomment this line to use console.log
// import "hardhat/console.sol";

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract ShippingAgreement {
    enum shipping_states{ SHIPPING, RECEIVED }

    shipping_states public state;
    
    // Requirements
    uint max_temp = 90;
    uint max_acc = 3;

    address payable public sender;
    address payable public shipper;
    address public recipient;

    uint reward_amount;
    ERC20 reward_token;
    uint fee_amount;
    uint penalty_amount = 0;

    constructor(
        address _shipper,
        address _recipient,
        address _reward_token_address,
        uint _reward_amount,
    ) payable {
        sender = payable(msg.sender);
        shipper = payable(_shipper);
        recipient = _recipient;
        reward_token = ERC20(_reward_token_address);
        
        fee_amount = _reward_amount / 100;
        
        Deposit 

        state = shipping_states.SHIPPING;
        // Deposit reward in smart contract
    }



    function receiveShipment(
        string calldata _temp,
        string calldata _acc,
        string calldata _signature
    ) public {
        require(msg.sender == recipient, "You are not the recipient"); // Only the recipient can receive the shipment

        uint penalty = 0;

        // Check signature


        // For each requirement decrease reward and increase penalty
        

        // checking to see if read temp has exceeded the set max_temp, if so removing a percent of the reward as penalty
        if _temp >= max_temp {
            penaltytemp = _temp - max_temp;
            penalty += penaltytemp*(reward_amount/100);
            
        }

        // checking to see if read acceleration has exceeded the set max_accel, if so removing a percent of the reward as penalty
        if _acc >= max_acc{
            penaltyacc = _acc - max_acc;
            penalty += penaltyacc*(reward_amount/10);
        }

        if penalty >= (reward_amount - fee_amount){
            reward_amount = 0;
            penalty_amount = reward_amount - fee_amount;
            
        } else {
            reward_amount = reward_amount - fee_amount - penalty;
        }
            
        state = shipping_states.RECEIVED;
    }

    function withdraw_reward() public {
        require(msg.sender == shipper, "You are not the shipper"); // Only the shipper can withdraw the reward
        require(state == shipping_states.RECEIVED, "Shipment not received"); // Shipment must be received

        // TODO send reward amount of reward token to shipper
    }

    function withdraw_penalty() public {
        require(msg.sender == sender, "You are not the sender"); // Only the sender can withdraw the penalty
        require(state == shipping_states.RECEIVED, "Shipment not received"); // Shipment must be received

        // TODO send penalty amount of reward token to sender
        

    }
}
