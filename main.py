import datetime
from twilio.rest import Client
from decouple import config

print('Starting Application')
# Function to send SMS using Twilio API
def send_sms(account_sid, auth_token, sender_phone_number, recipient_phone_number, message):
    # Log in to the Twilio API
    client = Client(account_sid, auth_token)

    # Send the message
    client.messages.create(
        to=recipient_phone_number,
        from_=sender_phone_number,
        body=message
    )

# Calculate the recommended daily water intake
def calculate_water_intake(age, weight, activity_level, steps, climate):
    # Calculate base water intake
    base_intake = weight * 0.033

    # Adjust for age
    if age < 30:
        age_factor = 40
    elif age < 55:
        age_factor = 35
    else:
        age_factor = 30

    intake = base_intake + (activity_level * steps / 1000) + age_factor

    # Adjust for climate
    if climate == 'Equitorial':
        intake *= 1.5
    elif climate == 'Temperate':
        intake *= 1
    elif climate == 'Arctic':
        intake *= 0.5

    return round(intake, 2)

# Set up the water reminder parameters
age = 24
weight = 99
activity_level = 1
steps = 8000
climate = 'Equitorial'

print('Generating Intake...')
recommended_intake = calculate_water_intake(age, weight, activity_level, steps, climate)

# Get the current time
now = datetime.datetime.now()

# Set the start and end times for the water reminder notifications
start_time = datetime.time(6, 0, 0)  # 6am
end_time = datetime.time(23, 0, 0)  # 11pm

# Check if it's within the notification period
if start_time <= now.time() <= end_time:

    today = datetime.datetime.today().strftime('%Y-%m-%d %H:%M')
    print('Sending Notification...')
    # Send the water reminder SMS
    account_sid = config('account_sid')
    auth_token = config('auth_token')
    sender_phone_number = config('sender_phone_number')
    recipient_phone_number = config('recipient_phone_number')
    message = 'It\'s time to drink water! Recommended 3 Hours intake: {} liters. Sent at {}'.format(recommended_intake, today)
    send_sms(account_sid, auth_token, sender_phone_number, recipient_phone_number, message)
    print(f'Sent at {today}\n')

    # Log the reminder
    with open('reminder_log.txt', 'a') as f:
        f.write(today + '\n')
else:
    print('It is currently outside of the water reminder period (6am to 11pm).')
