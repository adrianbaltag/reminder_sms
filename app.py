from twilio.rest import Client
import config

client = Client(config.account_sid, config.auth_token)
""" for multiple phone#"""
phone_numbers = [config.number1, config.number2]
for phone_number in config.phone_numbers:
    call = client.messages.create(
        # number to send //use: +1phone#
        to=phone_number,
        #twilio number //use: +1phone#
        from_=config.twilio_number,
        body="maluma baby baby11111"
    )
print(config.phone_numbers)


