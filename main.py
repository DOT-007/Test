from flask import Flask, request, render_template, redirect, url_for
import telebot
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app and Telebot
app = Flask(__name__)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Initialize the bot with the loaded token
bot = telebot.TeleBot(TOKEN)

@app.route('/')
def index():
    # Render the contact form
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve data from the form
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Format message for Telegram
    telegram_message = f"New Contact Submission:\nName: {name}\nEmail: {email}\nMessage: {message}"

    # Send message to Telegram
    bot.send_message(CHAT_ID, telegram_message)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
