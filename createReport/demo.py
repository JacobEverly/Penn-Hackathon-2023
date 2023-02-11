# SPDX-FileCopyrightText: Copyright (c) 2021 David Glaude
#
# SPDX-License-Identifier: Unlicense
from time import sleep
from datetime import datetime
import subprocess
# from ecdsa import SigningKey
from web3.auto import w3
from eth_abi.packed import encode_abi_packed
from eth_utils import keccak
from eth_account.messages import encode_defunct
from web3 import Web3, Account


import requests
import json
import web3

# from web3 import Web3



# sk = SigningKey.generate()
# vk = sk.verifying_key

print("""\

  _____              _                         _______                 _               
 |  __ \            | |                       |__   __|               | |              
 | |__) |__ _   ___ | | __ __ _   __ _   ___     | | _ __  __ _   ___ | | __ ___  _ __ 
 |  ___// _` | / __|| |/ // _` | / _` | / _ \    | || '__|/ _` | / __|| |/ // _ \| '__|
 | |   | (_| || (__ |   <| (_| || (_| ||  __/    | || |  | (_| || (__ |   <|  __/| |   
 |_|    \__,_| \___||_|\_\\__,_| \__, | \___|    |_||_|   \__,_| \___||_|\_\\___||_|   
                                  __/ |                                                
                                 |___/                                                 


""")

# print("🔑 Secret Key:")
# print(sk.to_string().hex())
print("🔑 Secret Key:")
private_key = "0x4d9e599423f0a37115c35f1dc4b749a4754545e4172d3901260a484512eee4d6"
print(private_key)






# print("🔑 Public Key:")
# print(vk.to_string().hex())


# report=f'Time: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")} - Max acc: {2} - Max Temp: {80}'

temp = "80"
acc = "2"
report = temp+"-"+acc

print(report)

# hash = keccak(report.encode())
message = encode_defunct(text=report)
# message = encode_defunct(text=temp,"-",acc)

signed_message =  w3.eth.account.sign_message(message, private_key= private_key)



# signature = sk.sign(report.encode('UTF-8'))

# msg = f"Report: [{report}] Signature {signature.hex()}"
print("*********************")
print(len(signed_message.signature))

print(signed_message)


