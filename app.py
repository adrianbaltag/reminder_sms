from twilio.rest import Client
import config


client = Client(config.account_sid, config.auth_token)

call = client.messages.create(
    # number to send //use: +1phone#
    to=config.number1,
    #twilio number //use: +1phone#
    from_=config.twilio_number,
    body="tadaaa"
)
