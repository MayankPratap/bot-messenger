import requests
import json
from core.postback_message import ButtonMessage

#save token in enviroment variable or in database, bad practice to initialize here.
token = "EAAF96u7EUXIBAL9sskjA1ZC3UyNwEjby116a3wBIFJLdoTvA02S3xrTj3sTAvZAuKWd8isVRknXswxSjGGFkrvCI4YdLngybZCgB0K7BnIZCFhJAxdqluFSruEPQQhVdZCaB1AoxDtNKyOxacUQfvPIL92zziOZAWCyq2ouxtYbQZDZD"

class DispatchMessage:

    def __init__(self, image_url):
        self.image_url = image_url

    def dispatch_message(self):

        #for testing purpose we will have a list which contains facebook numeric ids of testors and message will be sent only to them

        fbids = ['100000916344472', '100008872294514']

        #we are going to have same attachment for all users
        attachment = ButtonMessage(self.image_url)
        save_attachment = attachment.attachment_message()


        for ids in fbids:

            payload = {'recipient': {'id': ids}, 'message': save_attachment}  # We're going to send this back
            r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)  # Lets send it

            print r.status_code