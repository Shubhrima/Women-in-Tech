from flask import Flask, render_template, flash,request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, SelectField
from wtforms.validators import DataRequired, URL
import csv
import requests
import unicodedata
from smtplib import SMTP

OWN_EMAIL='sjanainfo1@gmail.com'
OWN_PASSWORD='information6**'


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

@app.route("/")
def home():
    response = requests.get('https://api.npoint.io/2a8a1433b5b26184d7b5')
    posts = response.json()
    return render_template('index.html', posts=posts)

@app.route('/form', methods=["POST"])
def get_data_from_form():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    send_email(name, email, phone, message)
    flash('Thank you!!')
    return render_template("index.html", msg_sent=True)

@app.route("/contact")
def contact():
    if request.method == "POST":
        data = request.form
        print('reached')
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):

    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, 'shubhrijana@gmail.com', email_message)

if __name__=='__main__':
    app.run(debug=True)