import os
import smtplib
import email.message
from flask import Flask

import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

key = "AIzaSyDAQDS5fLJ5HpUJT-j59rc0FoNFvgnRtmE"
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-1.5-flash')

contacts = ['marigumerpr@gmail.com', 'narutogbzlol@gmail.com']

def to_markdown(text):
  text = text.replace('•', '')
  text = text.replace(':', '<br/>')
  return Markdown(textwrap.indent(text, '\n', predicate=lambda _: True))

# Texto de entrada

app = Flask(__name__)

@app.route("/")
def index():
  send_email(contacts)
  return "send"

def generate():
  response = model.generate_content("Give me 5 curiosities about ducks, in portuguese, formated in HTML5")
  return response.text

def send_email(contacts):  
    email_text = generate()
    
    for i in contacts:
      msg = email.message.Message()
      msg['Subject'] = "Sua fonte de curiosidades sobre patos :)"
      msg['From'] = 'myemailbot999@gmail.com'
      msg.set_payload(to_markdown(email_text).data)
      msg.add_header('Content-Type', 'text/html')
      password = 'buqgsrnqrxjjiggq'
      s = smtplib.SMTP('smtp.gmail.com: 587')
      s.starttls()
      s.login(msg['From'], password)
      msg['To'] = i
      print(msg['To'])
      s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    return email_text

if __name__=="__main__":
    app.run(debug=True, use_reloader=False)


