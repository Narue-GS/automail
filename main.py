import smtplib
import email.message
from flask import Flask

from transformers import GPT2Tokenizer, GPT2Model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')
text = "Say something funny about ducks"
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
response = tokenizer.decode(output[0], skip_special_tokens=True)
print(response)

# Texto de entrada

# app = Flask(__name__)

# @app.route("/")
# def index():
#   return send_email()

# def generate():
#     input_text = "Give me a curiosity about ducks"
#     input_ids = tokenizer.encode(input_text, return_tensors='pt')

#     output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)

#     response = tokenizer.decode(output[0], skip_special_tokens=True)
#     return response

# def send_email():  
#     email_text = generate()
#     msg = email.message.Message()
#     msg['Subject'] = "Assunto"
#     msg['From'] = 'myemailbot999@gmail.com'
#     msg['To'] = 'narutogbzlol@gmail.com'
#     password = 'buqgsrnqrxjjiggq'
#     msg.add_header('Content-Type', 'text/html')
#     msg.set_payload(email_text)

#     s = smtplib.SMTP('smtp.gmail.com: 587')
#     s.starttls()
#     s.login(msg['From'], password)
#     s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
#     return email_text

# if __name__=="__main__":
#     app.run(debug=True, use_reloader=False)


