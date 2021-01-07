import time
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message
from selenium.webdriver.support.ui import WebDriverWait
driver = WhatsAPIDriver()
print("Waiting for QR")

time.sleep(30)

print("Bot started")


while True:
    time.sleep(3)
    print("Checking for more messages")
    for contact in driver.get_unread():
        for message in contact.messages:
            if isinstance(message, Message):  # Currently works for text messages only.
                contact.chat.send_message(message.content)
