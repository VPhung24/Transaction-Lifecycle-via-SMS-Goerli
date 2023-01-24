# -*- coding: utf-8 -*-
import os
from flask import Flask, request, render_template, url_for, redirect
from twilio.rest import Client
from helper import account_sid, auth_token, from_phone_number, to_phone_number, Chain, subscribeToChain, ChainInfo
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, PasswordField, SelectField)
from wtforms.validators import DataRequired, Length

client = Client(account_sid, auth_token)

app = Flask(__name__, template_folder='templates')
bootstrap = Bootstrap5(app)
app.debug = True
app.config.update(dict(
    SECRET_KEY=os.getenv('SECRET_KEY'),
    WTF_CSRF_SECRET_KEY=os.getenv('WTF_CSRF_SECRET_KEY')
))


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
                                         blockNum + " \n Check tx: " + subscribeToChain.block_explorer_url + hash, from_=from_phone_number, to=to_phone_number)
        print(message.sid)

    form = LoginForm(request.form)
    return render_template('index.html', form=form)


@app.route('/helloWorld/')
def hello_world():
    return 'Hello World!'


@app.route('/readme/')
def read_me():
    return 'read me!'


@app.route('/pears/')
def pears():
    return 'pears'


class LoginForm(FlaskForm):
    tx = StringField('tx', validators=[
        DataRequired(), Length(64)])
    chain = SelectField(
        choices=[('Polygon', 'Polygon'), ('Ethereum', 'Ethereum'), ('Goerli', 'Goerli')])
    submit = SubmitField()


def run():
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
