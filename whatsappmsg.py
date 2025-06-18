from twilio.rest import Client
from datetime import datetime, timedelta
import time

#account_sid = 'AC745ad82a0c331b6cadaca2969c046784'
#auth_token = '2e948479b4c9f80e501319f33279a35f'

#client = Client(account_sid, auth_token)

def whatsapp_msg(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message ID: {message.sid}')
    except Exception as e:
        print(f"An error occurred: {e}")

name = input('Enter the recipient name: ')
recipient_number = input("Enter the recipient WhatsApp number with country code: ")
message_body = input(f'Enter the message you want to send to {name}: ')

date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24-hour format): ')

# Parse and calculate delay
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('The specified time is in the past. Please enter a future date and time.')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')
    time.sleep(delay_seconds)
    whatsapp_msg(recipient_number, message_body)
