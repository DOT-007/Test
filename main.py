from flask import Flask, request, render_template, redirect, url_for
import telebot
import os

# Initialize Flask app and Telebot
app = Flask(__name__)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telebot.TeleBot(TOKEN)

@app.route('/')
def index():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    telegram_message = f"New Contact Submission:\nName: {name}\nEmail: {email}\nMessage: {message}"
    bot.send_message(CHAT_ID, telegram_message)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
