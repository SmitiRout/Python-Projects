#twilio library helps to get the feature to send the whatsapp message. twilio gives facility to send whatsapp message , call and text.

""""
modules used in this project:
twilio
datetime module
time module
"""

"""
1. twilio client setup
2. user input
3. scheduling logic
4.send message
"""

#step1 intsall required libraries
from twilio.rest import Client
from datetime import datetime
import time

"""
Modules used in this project:
- twilio
- datetime
- time
"""

# Step 1: Twilio credentials
account_sid = ''     #YOU WILL RECEIVE AFTER YOU LOGIN IN TWILIO
auth_token = ''

client = Client(account_sid, auth_token)

# Step 2: Define the function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print('An error occurred:', e)

# Step 3: User input
name = input('Enter the recipient name: ')
recipient_number = input('Enter the recipient WhatsApp number with country code (e.g.; +91): ')
message_body = input(f'Enter the message you want to send to {name}: ')

# Step 4: Get date and time
date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24-hour format): ')

#datetime module overview : use to efficiently handle time and date

try:
    schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")          
     #strptime function is used to convert the string in date time object.
     #syntax= datetime.strptime( {date_str} , format)
     
    current_datetime = datetime.now()               #used to calculate the current time
    delay_seconds = (schedule_datetime - current_datetime).total_seconds()             #this function is used  to convert the remaining time into seconds.
    

    if delay_seconds <= 0:
        print('The specified time is in the past. Please enter a future date and time.')
    else:
        print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')
        time.sleep(delay_seconds)
        send_whatsapp_message(recipient_number, message_body)

except ValueError:
    print("Invalid date or time format. Please use YYYY-MM-DD and HH:MM.")


