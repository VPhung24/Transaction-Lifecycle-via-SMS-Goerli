import os
import json
import time
from websocket import create_connection
from twilio.rest import Client
import pickle
from helper import account_sid, auth_token, from_phone_number, to_phone_number, subscribeToChain, ChainInfo

client = Client(account_sid, auth_token)

for i in range(3):
    try:
        ws = create_connection(
            subscribeToChain.websocket_url + subscribeToChain.alchemy_key)
        print("Connection made")
    except Exception as error:
        print('Connection Error: ' + repr(error))
        time.sleep(3)
    else:
        break

ws.send(json.dumps({"jsonrpc": "2.0", "method": "eth_subscribe", "params": [
        "alchemy_filteredNewFullPendingTransactions", {"address": os.getenv('ETH_WALLET_ADDRESS_FOR_SUBSCRIPTION')}], "id": 1}))
print("JSON eth_subscribe sent")

while True:
    try:
        result = ws.recv()
        result = json.loads(result)["params"]["result"]
        from_address = (result["from"])
        to_address = (result["to"])
        hash = (result["hash"])
        blockHash = (result["blockNumber"])

        print("from:", from_address)
        print("to:", to_address)
        print("hash: ", hash)
        print("blockHash: ", blockHash)

        print("Send Twilio SMS for pending transaction!")
        message = client.messages \
            .create(
                body="\n \n PENDING TX! \n\n From: " + from_address +
                " \n\n To: " + to_address + "\n\n  @tx:" + hash,
                from_=from_phone_number,
                to=to_phone_number
            )

        print(message.sid)

    except KeyError as error:
        print("Check JSON params for parsing")

    except Exception as error:
        print('JSON Error: ' + repr(error))
        time.sleep(1)

ws.close()
