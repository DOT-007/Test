from flask import Flask, request, render_template, redirect, url_for
import telebot

# Initialize Flask app and Telebot
app = Flask(__name__)
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

# Replace with your chat ID
CHAT_ID = "YOUR_CHAT_ID"

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
