from flask import Flask, request
import requests
import json
import traceback
import random
from core.dispatch_message import DispatchMessage


app = Flask(__name__)
# Raula machega
#bhai upar line ka matlab kya h?
token = "EAAF96u7EUXIBAL9sskjA1ZC3UyNwEjby116a3wBIFJLdoTvA02S3xrTj3sTAvZAuKWd8isVRknXswxSjGGFkrvCI4YdLngybZCgB0K7BnIZCFhJAxdqluFSruEPQQhVdZCaB1AoxDtNKyOxacUQfvPIL92zziOZAWCyq2ouxtYbQZDZD"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
  if request.method == 'POST':
    try:
      data = json.loads(request.data)
      text = data['entry'][0]['messaging'][0]['message']['text'] # Incoming Message Text
      sender = data['entry'][0]['messaging'][0]['sender']['id'] # Sender ID
      payload = {'recipient': {'id': sender}, 'message': {'text': sender}} # We're going to send this back
      r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload) # Lets send it
    except Exception as e:
      print traceback.format_exc() # something went wrong
  elif request.method == 'GET': # For the initial verification
    if request.args.get('hub.verify_token') == 'iamsherlock':
      return request.args.get('hub.challenge')
    return "Wrong Verify Token"
  return "Hello World" #Not Really Necessary

@app.route('/dispatch_message', methods=['GET', 'POST'])
    #we will build messages weather image is sent, if image is not there in post data, then message won't get dispatched.
def dispatch_message():

    if request.method == "POST":
        data = json.loads(request.data)
        dispatch_message = DispatchMessage(data.POST['image_url'])
        dispatch_message.dispatch_message()

        return 200


if __name__ == '__main__':
  app.run(debug=True)
