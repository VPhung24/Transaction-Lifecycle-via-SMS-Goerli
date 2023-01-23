import json
import time
from websocket import create_connection
import os
from twilio.rest import Client
import pickle

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)
alchemy_key = os.getenv('ALCHEMY_KEY')
from_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
to_phone_number = os.getenv('TWILIO_SEND_UPDATES_TO_PHONE_NUMBER')

for i in range(3):
    try:
        ws = create_connection(
            "wss://eth-goerli.g.alchemy.com/v2/"+alchemy_key)
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
        result = json.loads(result)
        from_address = (result["params"]["result"]["from"])
        to_address = (result["params"]["result"]["to"])
        hash = (result["params"]["result"]["hash"])
        blockHash = (result["params"]["result"]["blockNumber"])

        # data = pickle.load( open( "data.p", "rb" ) )
        # data.add(hash)
        # pickle.dump(data, open( "data.p", "wb" ) )

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

        # data = pickle.load( open( "data.p", "rb" ) )
        # print(data)

    except KeyError as error:
        print("Check JSON params for parsing")

    except Exception as error:
        print('JSON Error: ' + repr(error))
        time.sleep(1)

ws.close()
