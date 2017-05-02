from flask import Flask, request
from pymessenger.bot import Bot
import requests
import json
import traceback
import random
app = Flask(__name__)
# Raula machega
access_token="EAAF96u7EUXIBAL9sskjA1ZC3UyNwEjby116a3wBIFJLdoTvA02S3xrTj3sTAvZAuKWd8isVRknXswxSjGGFkrvCI4YdLngybZCgB0K7BnIZCFhJAxdqluFSruEPQQhVdZCaB1AoxDtNKyOxacUQfvPIL92zziOZAWCyq2ouxtYbQZDZD"
recipient_id="1442034082522401"

text=""

@app.route('/gotsomepic',methods=['GET','POST'])
def gotsomepic():
	if request.method=='POST':
		global text
		text=""
		data=request.data.decode('utf-8')
		data=json.loads(data)
		image_url=data['image_url']
		print(image_url)
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
		image_url ="http://orig03.deviantart.net/c543/f/2011/103/4/7/mystic____gohan_by_drozdoo-d3dxa17.png"
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

	return "Everything's OK"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
	global text
	text=""
	if request.method == 'POST':
		try:
			data=request.data.decode('utf-8')   # Python 3 me bytes ka chakkar hota hai 
			data=json.loads(data)
			#data = json.loads(request.data)
			text = data['entry'][0]['messaging'][0]['message']['text'] # Incoming Message Text
			sender = data['entry'][0]['messaging'][0]['sender']['id'] # Sender ID
			#payload = {'recipient': {'id': sender}, 'message': {'text': sender}} # We're going to send this back
			#r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + access_token, json=payload) # Lets send it
			
		except Exception as e:
			print(traceback.format_exc()) # something went wrong
	elif request.method == 'GET': # For the initial verification
		if request.args.get('hub.verify_token') == 'marksuckerberg':
			return request.args.get('hub.challenge')
		return "Wrong Verify Token"
	return "Everything's OK"


@app.route('/userReply',methods=['GET'])

def userReply():
	global text
	if request.method=='GET':
		if text=="No":
			text=""
			return "No"
		elif text=="Yes":
			text=""
			return "Yes"
		else:
			return ""



if __name__ == '__main__':
	app.run(debug=True)
