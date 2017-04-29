class ButtonMessage:

    def __init(self, image_url):

        self.image = image_url

    def attachment_message(self):

        message_attachment = {}
        message_attachment['attachment'] = {}
        message_attachment['attachment']['type'] = 'file'
        message_attachment['attachment']['payload'] = {}
        message_attachment['attachment']['payload']['url'] = "" #here we will give url for payload

        return message_attachment