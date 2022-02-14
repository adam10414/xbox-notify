from twilio.rest import Client

from auth.auth import account_sid, auth_token


def send_sms_notification(sms_message, to_number):
    """
    Send an SMS message to a number of your choosing.
    Returns a message obj after sending a POST to the Twilio URI
    message: str
    to: str - '+12223334444'
    """

    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body=sms_message,
                     from_='+18126248412',
                     to=to_number
                 )

    return message