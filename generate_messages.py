import csv  # Module to work with CSV files
import os  # Module for interacting with the operating system (not used here, but imported)
from twilio.rest import Client  # Twilio library for interacting with their API

# Twilio account credentials (replace with actual credentials)
account_sid = ''  # Your Twilio Account SID which is given to you on the website.
auth_token = ''  # Your Twilio Auth Token which is also given to you on the website.

# Initialize the Twilio Client with the credentials
Client = Client(account_sid, auth_token)

# Function to load data from a CSV file
def load_data(filename):
    mylist = []  # List to store rows of data from the CSV file
    with open(filename) as example:  # Open the CSV file in read mode
        example_data = csv.reader(example, delimiter=',')  # Read CSV data with ',' as the delimiter
        next(example_data)  # Skip the header row of the CSV file
        for row in example_data:  # Iterate through each row in the CSV
            mylist.append(row)  # Append each row to the list
    return mylist  # Return the list containing all the rows of data

# Load patient data from a CSV file (adjust the path as necessary)
new_list = load_data(r'')

# Iterate over each patient's data in the list
for row in new_list:
    # Send a personalized SMS message to the patient's phone number
    messages = Client.messages\
                .create(
                    body=f"Hey, {row[0]} our records show you failed to attend your appointment. Please call us on........ to reschedule your appointment. Thanks.",  # Message content
                    from_= '',  # Twilio phone number (replace with an active number)
                    to= row[2]  # Recipient's phone number from the CSV file (index 2 of the row)
                )
    # Print the SID of the sent message to verify success
    print(messages.sid)

# TO DO: Buy a Twilio number for $3/month to send messages to unverified numbers and pay for message fees.


