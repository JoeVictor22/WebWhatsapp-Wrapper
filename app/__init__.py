from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import qrcode
import base64
from io import BytesIO

import json
import os
import sys
import time
from pprint import pprint
from webwhatsapi import WhatsAPIDriver

app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)


from app.models.contatoTable import Contato
from app.models.sessaoTable import Sessao
from app.models.mensagemTable import Mensagem

from app.controllers import routes


## API ROUTINE

print("Environment", os.environ)
try:
    os.environ["SELENIUM"]
except KeyError:
    print("Please set the environment variable SELENIUM to Selenium URL")
    sys.exit(1)

##Save session on "/firefox_cache/localStorage.json".
##Create the directory "/firefox_cache", it's on .gitignore
##The "app" directory is internal to docker, it corresponds to the root of the project.
##The profile parameter requires a directory not a file.
profiledir = os.path.join(".", "firefox_cache")
if not os.path.exists(profiledir):
    os.makedirs(profiledir)

driver = WhatsAPIDriver(
    profile=profiledir, client="remote", command_executor=os.environ["SELENIUM"]
)

qr = driver.get_qr_plain()
print(qr)
'''
contato = Contato.query.get(1)

if contato is None:
    print("nao existe")
else:
    contato.qr_code = qr
    print("QR SALVO")
'''
img = qrcode.make(qr)
buffered = BytesIO()
img.save(buffered, format="png")
img_str = base64.b64encode(buffered.getvalue())

time.sleep(1)
print("Waiting for QR")
driver.wait_for_login()
print("Saving session")
driver.save_firefox_profile(remove_old=False)
print("Bot started")

while True:
    time.sleep(3)
    print("Checking for more messages, status", driver.get_status())

    for contact in driver.get_unread():
        pprint(contact)
        for message in contact.messages:
            text = "Sei lá"
            driver.send_message_to_id(message.chat_id, text)
            print(json.dumps(message.get_js_obj(), indent=4))
            print("class", message.__class__.__name__)
            print("message", message)
            print("id", message.id)
            print("type", message.type)
            print("timestamp", message.timestamp)
            print("chat_id", message.chat_id)
            print("sender", message.sender)
            print("sender.id", message.sender.id)
            print("sender.safe_name", message.sender.get_safe_name())
            if message.type == "chat":
                print("-- Chat")
                print("safe_content", message.safe_content)
                print("content", message.content)
                # contact.chat.send_message(message.safe_content)
            elif message.type == "image" or message.type == "video":
                print("-- Image or Video")
                print("filename", message.filename)
                print("size", message.size)
                print("mime", message.mime)
                print("caption", message.caption)
                print("client_url", message.client_url)
                message.save_media("./")
            else:
                print("-- Other")
