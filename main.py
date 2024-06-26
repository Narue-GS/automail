import smtplib
import email.message
from flask import Flask

from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Carregar o modelo e o tokenizador
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Texto de entrada
input_text = "Explique o processo de fotossíntese."

# Codificar o texto de entrada
input_ids = tokenizer.encode(input_text, return_tensors='pt')

# Gerar a resposta
output = model.generate(input_ids, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)

# Decodificar e imprimir a resposta
response = tokenizer.decode(output[0], skip_special_tokens=True)
print(response)


# app = Flask(__name__)

# @app.route("/")
# def index():
#     send_email()
#     return "running"


# def send_email():  
#     email_text = """
#         <h1>Hey bro</h1></br>
#         <p>What's up?</p>
#     """

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
#     print('Email enviado')

# if __name__=="__main__":
#     app.run(debug=True, use_reloader=False)

