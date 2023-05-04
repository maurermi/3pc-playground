from web3 import Web3, HTTPProvider
from flask import Flask, render_template, request

hostName = "10.29.32.154"
serverPort = 8081

app = Flask(__name__)
w3 = Web3(HTTPProvider('http://10.29.32.154:8888/'))
faucet_addr = "0x6A76bC9CC5eF587cc2b6F998f60db606631DE48c"
caller = "0x01A151CC5ED14d110cc0e6b64360913DE9f453F1"
PK = "32a49a8408806e7a2862bca482c7aabd27e846f673edc8fb0000000000000000"
abi = [{
    "inputs": [],
    "stateMutability": "nonpayable",
    "type": "constructor"
},
    {
    "anonymous": False,
    "inputs": [
        {
            "indexed": True,
            "internalType": "address",
            "name": "owner",
                    "type": "address"
        },
        {
            "indexed": True,
            "internalType": "address",
            "name": "spender",
                    "type": "address"
        },
        {
            "indexed": False,
            "internalType": "uint256",
            "name": "value",
                    "type": "uint256"
        }
    ],
    "name": "Approval",
    "type": "event"
},
    {
    "anonymous": False,
    "inputs": [
        {
            "indexed": True,
            "internalType": "address",
            "name": "from",
                    "type": "address"
        },
        {
            "indexed": True,
            "internalType": "address",
            "name": "to",
                    "type": "address"
        },
        {
            "indexed": False,
            "internalType": "uint256",
            "name": "value",
                    "type": "uint256"
        }
    ],
    "name": "Transfer",
    "type": "event"
},
    {
    "inputs": [
        {
            "internalType": "address",
            "name": "owner",
            "type": "address"
        },
        {
            "internalType": "address",
            "name": "spender",
            "type": "address"
        }
    ],
    "name": "allowance",
    "outputs": [
        {
            "internalType": "uint256",
            "name": "",
            "type": "uint256"
        }
    ],
    "stateMutability": "view",
    "type": "function"
},
    {
    "inputs": [
        {
            "internalType": "address",
            "name": "spender",
            "type": "address"
        },
        {
            "internalType": "uint256",
            "name": "amount",
            "type": "uint256"
        }
    ],
    "name": "approve",
    "outputs": [
        {
            "internalType": "bool",
            "name": "",
            "type": "bool"
        }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
},
    {
    "inputs": [
        {
            "internalType": "address",
            "name": "account",
            "type": "address"
        }
    ],
    "name": "balanceOf",
    "outputs": [
        {
            "internalType": "uint256",
            "name": "",
            "type": "uint256"
        }
    ],
    "stateMutability": "view",
    "type": "function"
},
    {
    "inputs": [],
    "name": "decimals",
    "outputs": [
        {
            "internalType": "uint8",
            "name": "",
                    "type": "uint8"
        }
    ],
    "stateMutability": "view",
    "type": "function"
},
    {
    "inputs": [
        {
            "internalType": "address",
            "name": "spender",
            "type": "address"
        },
        {
            "internalType": "uint256",
            "name": "subtractedValue",
            "type": "uint256"
        }
    ],
    "name": "decreaseAllowance",
    "outputs": [
        {
            "internalType": "bool",
            "name": "",
            "type": "bool"
        }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
},
    {
    "inputs": [
        {
            "internalType": "address",
            "name": "spender",
            "type": "address"
        },
        {
            "internalType": "uint256",
            "name": "addedValue",
            "type": "uint256"
        }
    ],
    "name": "increaseAllowance",
    "outputs": [
        {
            "internalType": "bool",
            "name": "",
            "type": "bool"
        }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
},
    {
    "inputs": [],
    "name": "name",
    "outputs": [
        {
            "internalType": "string",
            "name": "",
                    "type": "string"
        }
    ],
    "stateMutability": "view",
    "type": "function"
},
    {
    "inputs": [
        {
            "internalType": "address",
            "name": "requestor",
            "type": "address"
        }
    ],
    "name": "requestTokens",
    "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
},
    {
    "inputs": [],
    "name": "symbol",
    "outputs": [
        {
            "internalType": "string",
            "name": "",
                    "type": "string"
        }
    ],
    "stateMutability": "view",
    "type": "function"
},
    {
    "inputs": [],
    "name": "totalSupply",
    "outputs": [
        {
            "internalType": "uint256",
            "name": "",
                    "type": "uint256"
        }
    ],
    "stateMutability": "view",
    "type": "function"
},
    {
    "inputs": [
        {
            "internalType": "address",
            "name": "to",
            "type": "address"
        },
        {
            "internalType": "uint256",
            "name": "amount",
            "type": "uint256"
        }
    ],
    "name": "transfer",
    "outputs": [
        {
            "internalType": "bool",
            "name": "",
            "type": "bool"
        }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
},
    {
    "inputs": [
        {
            "internalType": "address",
            "name": "from",
            "type": "address"
        },
        {
            "internalType": "address",
            "name": "to",
            "type": "address"
        },
        {
            "internalType": "uint256",
            "name": "amount",
            "type": "uint256"
        }
    ],
    "name": "transferFrom",
    "outputs": [
        {
            "internalType": "bool",
            "name": "",
            "type": "bool"
        }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
}
]

chainid = w3.eth.chain_id

faucet = w3.eth.contract(address=faucet_addr, abi=abi)

# homepage
@app.route('/')
def index():
    return render_template('homepage.html')


# handle post requests
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    try:
        nonce = w3.eth.get_transaction_count(caller)
        call_func = faucet.functions.requestTokens(text).build_transaction({
            "chainId": chainid, "from": caller, "nonce": nonce})
        signed_tx = w3.eth.account.sign_transaction(call_func, private_key=PK)
        send_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(send_tx)
        return render_template('success.html')
    except:
        print('error handled')
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True, host=hostName, port=serverPort)
