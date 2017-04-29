from flask import Flask, request
from pymessenger.bot import Bot
import requests
import json
import traceback
import random
app = Flask(__name__)
# Raula machega
access_token = "EAAF96u7EUXIBAL9sskjA1ZC3UyNwEjby116a3wBIFJLdoTvA02S3xrTj3sTAvZAuKWd8isVRknXswxSjGGFkrvCI4YdLngybZCgB0K7BnIZCFhJAxdqluFSruEPQQhVdZCaB1AoxDtNKyOxacUQfvPIL92zziOZAWCyq2ouxtYbQZDZD"
recipient_id="1442034082522401"

@app.route('/gotsomepic',methods=['GET','POST'])
def gotsomepic():
  if request.method=='POST':
    #bot=Bot(access_token)
    #message="Aur bot kaise ho?" 
    #bot.send_text_message(recipient_id,message)
    image_url = "http://media1.santabanta.com/full1/Global%20Celebrities%28F%29/Sunny%20Leone/sunny-leone-127a.jpg"
    #elements = []
    #element = Element(title="tutorialPointRGB", image_url="https://www.tutorialspoint.com/dip/images/rgb.jpg", subtitle="")
    #elements.append(element)
    #bot.send_generic_message(recipient_id, elements)
    #payload = {'recipient': {'id': recipient_id}, 'message': {'text': "Code,Sleep,Repeat"}} # We're going to send this back
    element= {
        "title": "Someone at your door",
        "image_url": image_url,
        "subtitle": ""
    }
    
    elements=[element]

    message = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": elements
            }
        }
    }
    payload={'recipient':{'id':recipient_id},'message':message}
    r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + access_token, json=payload) # Lets send it
  else:
    #bot=Bot(access_token)
    #message="Aur bot kaise ho?" 
    #bot.send_text_message(recipient_id,message)
    image_url = "http://media1.santabanta.com/full1/Global%20Celebrities%28F%29/Sunny%20Leone/sunny-leone-127a.jpg"
    #bot.send_image_url(recipient_id, image_url)
    #elements = []
    #element = Element(title="tutorialPointRGB", image_url="https://www.tutorialspoint.com/dip/images/rgb.jpg", subtitle="")
    #elements.append(element)
    #bot.send_generic_message(recipient_id, elements)
    #payload = {'recipient': {'id': recipient_id}, 'message': {'text': "Code,Sleep,Repeat"}} # We're going to send this back
    #r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + access_token, json=payload) # Lets send it
    element= {
        "title": "Someone at your door",
        "image_url": image_url,
        "subtitle": ""
    }
    
    elements=[element]

    message = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": elements
            }
        }
    }
    payload={'recipient':{'id':recipient_id},'message':message}
    r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + access_token, json=payload) # Lets send it

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
  if request.method == 'POST':
    try:
      data = json.loads(request.data)
      text = data['entry'][0]['messaging'][0]['message']['text'] # Incoming Message Text
      sender = data['entry'][0]['messaging'][0]['sender']['id'] # Sender ID
      payload = {'recipient': {'id': sender}, 'message': {'text': sender}} # We're going to send this back
      r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + access_token, json=payload) # Lets send it
    except Exception as e:
      print traceback.format_exc() # something went wrong
  elif request.method == 'GET': # For the initial verification
    if request.args.get('hub.verify_token') == 'iamsherlock':
      return request.args.get('hub.challenge')
    return "Wrong Verify Token"
  return "Hello World" #Not Really Necessary

if __name__ == '__main__':
  app.run(debug=True)
