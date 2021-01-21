from app import app, db
import qrcode
import base64
from io import BytesIO
from flask import Flask, send_file, render_template

@app.route('/')
def hello_world():
    return 'Hello, World! from selenium'

