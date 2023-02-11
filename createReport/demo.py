# SPDX-FileCopyrightText: Copyright (c) 2021 David Glaude
#
# SPDX-License-Identifier: Unlicense
from time import sleep
from datetime import datetime
import subprocess
from ecdsa import SigningKey
from web3 import Web3


sk = SigningKey.generate()
vk = sk.verifying_key

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

print("🔑 Secret Key:")
print(sk.to_string().hex())
print("🔑 Public Key:")
print(vk.to_string().hex())


report=f'Time: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")} - Max acc: {2} - Max Temp: {80}'
signature = sk.sign(report.encode('UTF-8'))

msg = f"Report: [{report}] Signature {signature.hex()}"

print(len(signature))

print(msg)


