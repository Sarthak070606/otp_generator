from flask import *
from flask_mail import *
from random import *
import json
good = Flask(__name__)

with open('config.json', 'r') as f:
    parameter = json.load(f)['parameter']
good.config['MAIL_SERVER'] = 'smtp.gmail.com'
good.config['MAIL_PORT'] = 465
good.config['MAIL_USERNAME'] = parameter['gmail-user']
good.config['MAIL_PASSWORD'] = parameter['gmail-password']
good.config['MAIL_USE_TLS'] = False
good.config['MAIL_USE_SSL'] = True

mail = Mail(good)
otp = randint(100000, 999999)

@good.route("/")
def index():
    return render_template("email.html" , msg = " ")

@good.route("/submit-email", methods=["POST"])

def verify():
    email = request.form['email']
    msg = Message('OTP', sender ="jainsarthak517@gmail.com",recipients =[email])
    msg.body = str(otp)
    mail.send(msg)
    return render_template("verify.html")

@good.route('/verify', methods=["POST"])
def validate():
    user_OTP = request.form['otp']
    if otp == int(user_OTP):
        return  render_template("success.html" , msg = ' Email Verified Successfully ')
    else:
        return render_template(  "verify.html", msg="Not Verified  Try Again \n "
                                                    " Please enter the correct OTP ")

if "__main__" == __name__:
    good.run(debug= True)