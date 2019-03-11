# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("AC2304668ace933748c49383ac1b435635", "f76217a8211ba73896903c19358f3b11")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+923323117626", 
                       from_="+18044099816", 
                       body="Paisy rakh len Afghaani boti K!")
