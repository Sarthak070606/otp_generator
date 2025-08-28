📧 Flask OTP Email Verification

This is a simple Flask application to send OTP (One-Time Password) via Gmail and verify users' email addresses.

🚀 Features

Enter your email to receive an OTP

OTP is sent using Flask-Mail via Gmail

Verify OTP on the web page

Simple, lightweight, and beginner-friendly

🛠️ Tech Stack

Backend: Python, Flask

Email Service: Flask-Mail (Gmail SMTP)

Templates: HTML (Jinja2)

📂 Folder Structure
NyayaBot-OTP/
│
├─ projectflask.py        # Main Flask app
├─ config.json            # Gmail credentials
├─ requirements.txt       # Python dependencies
├─ README.md              # Documentation
├─ .gitignore             # Ignore unnecessary files
└─ templates/
   ├─ email.html          # Email input form
   ├─ verify.html         # OTP verification page
   └─ success.html        # Success page after OTP verification

⚙️ Setup Instructions
1. Clone the repository
git clone https://github.com/<your-username>/NyayaBot-OTP.git
cd NyayaBot-OTP

2. Create a virtual environment
python -m venv venv


Activate it:

Windows:

venv\Scripts\activate


macOS/Linux:

source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Configure Gmail credentials

Create a config.json file with your Gmail App Password:

{
  "parameter": {
    "gmail-user": "your_email@gmail.com",
    "gmail-password": "your_16_char_app_password"
  }
}


👉 Important: Use Gmail App Password, not your normal password.

5. Run the Flask app
python projectflask.py


Then open:
👉 http://127.0.0.1:5000/

✅ Notes

OTP is stored in memory (not database). For production, integrate with a database.

Requires App Password (enable 2FA in Gmail).

Simple HTML templates (email.html, verify.html, success.html) are included in the templates/ folder.

📜 License

This project is open-source and free to use.
