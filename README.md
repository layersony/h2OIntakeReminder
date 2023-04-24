# H20 Reminder
A Simple Python Script that reminds one to drink water after every 2 hours from 6am to 10pm or 11 pm

## How to use this
1. Clone the repository and cd into repository
2. Create a python virtual environment and install the requirements
```python
  python -m venv env_myh20
```
* Activate the environment
```python
  source env_myh20/bin/activate
```
* Install the requirements
```python
  pip install -r requirements.txt
```
3. Create a `.env` file and store you twilio Creds
```
account_sid='<account_sid>'
auth_token='<auth_token>'
sender_phone_number='<sender_phone_number>' # from twilio
recipient_phone_number='<recipient_phone_number>' # your phone number
```
4. Run the application
```
python3 main.py
```

5. To Notify you after every 2 hours we use a cronjob

* run in terminal
```
crontab -e
```
* Paste the following line into the editor opened
```
0 */2 6-22 * * <virtual_Environment_Path>/bin/python <File_path>/h2OIntakeReminder/main.py >> <File_path>/h2OIntakeReminder/h2Oreminder_cronjob.log 2>&1
```
`NB` remember to change the `File_Path` and `virtual_Environment_Path` to your own system path

* Restart the Cronjob service
```bash
sudo service cron restart
```

## Contact Me
Email - sammaingi5@gmail.com

