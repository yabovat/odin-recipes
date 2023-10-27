from twilio.twiml.messaging_response import Message, MessagingResponse
from flask import Flask, request, Response

app = Flask(__name)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # Create a MessagingResponse object to generate TwiML
    response = MessagingResponse()

    # Create a Message and set its body
    message = Message()
    message.body('Hello World!')

    # Append the Message to the Response
    response.append(message)

    # Redirect to a Twilio URL (optional)
    response.redirect('https://demo.twilio.com/welcome/sms/')

    # Convert the TwiML response to XML and send it back in the HTTP response
    return Response(str(response), content_type='application/xml')

if __name__ == '__main':
    app.run()
