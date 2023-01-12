from twilio.rest import Client
import config
import schedule
import time


def my_task():
    # Initialize the Twilio client
    client = Client(config.account_sid, config.auth_token)
    # or any other phone numbers
    phone_numbers = [config.number1, config.number2]
    for phone_number in phone_numbers:
        try:
            # Send the message
            message = client.messages.create(
                to=phone_number,
                from_=config.twilio_number,
                body="This is a test message"
            )
            print(f"Message sent to {phone_number}")
            if message.status == "failed" or message.status == "undelivered":
                print(f"An error occurred: {message.error_message}")
        except Exception as e:
            print(f"An error occurred: {e}")
            
schedule.every(2).minutes.do(my_task)  # replace the 1 with your desired value

while True:
    schedule.run_pending()
    time.sleep(1)



# evry day at a certain hour
# schedule.every().day.at("8:00").do(my_task)


# every certain interval(min,)
# schedule.every(1).minutes.do(my_task)
