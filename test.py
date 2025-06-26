from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import smtplib

# ✅ THIS MUST COME FIRST
load_dotenv()

# ✅ THEN get the keys
MAIL_ADDRESS = os.environ.get("EMAIL_KEY")
MAIL_APP_PW = os.environ.get("PASSWORD_KEY")

print(f"📧 MAIL: {MAIL_ADDRESS}")
print(f"🔑 PASSWORD LENGTH: {len(MAIL_APP_PW) if MAIL_APP_PW else 'None'}")
