# -*- coding: utf-8 -*-
import os
from flask import Flask, request
from twilio.rest import Client

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
to_phone_number = os.getenv('TWILIO_SEND_UPDATES_TO_PHONE_NUMBER')

client = Client(account_sid, auth_token)

app = Flask(__name__)
app.debug = True
queue = []


@app.route('/', methods=['POST', 'GET'])
def request_handler():
    print("Sending Twilio SMS for Mined transaction if webhook received!")
    if request.method == 'POST':
        data = (request.json)
        eventActivity = data['event']['activity']
        for i in range(len(eventActivity)):
            timestamp = data['createdAt']
            from_address = eventActivity[i]['fromAddress']
            to_address = eventActivity[i]['toAddress']
            blockNum = eventActivity[i]['blockNum']
            hash = eventActivity[i]['hash']

        print("DATA: ", data)
        print("HASH: ", hash)

        message = client.messages.create(body=" \n\n TX MINED! \n\n From: " + from_address + " \n\n To: " + to_address + " \n\n @#:" +
                                         blockNum + " \n Check tx: https://goerli.etherscan.io/tx/" + hash, from_=from_phone_number, to=to_phone_number)
        print(message.sid)

    return ("Ok")
    # return webhook(session), 200


def run():
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
