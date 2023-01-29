import smtplib
import email.message
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    send_email()
    return "running"

def send_email():  
    email_text = """
        <h1>Hey bro</h1></br>
        <p>What's up?</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'myemailbot999@gmail.com'
    msg['To'] = 'narutogbzlol@gmail.com'
    password = 'buqgsrnqrxjjiggq' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_text)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

if __name__=="__main__":
    app.run(debug=True, use_reloader=False)

