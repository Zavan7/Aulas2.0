import os
import pathlib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv 
import smtplib


load_dotenv()

#Caminho da mensagem de texto
CAMINHO_HTML = pathlib.Path(__file__).parent / 'texto.html'

#Dados do remetente e destinatario
remetente = os.getenv('FROM_EMAIL', '')
destinatário = remetente

#Dados do server SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem de texto
with open(CAMINHO_HTML, 'r', encoding = 'utf-8') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template (texto_arquivo)
    texto_email = template.substitute(nome = 'Vitor')

#Transformar nossa mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['From'] = remetente
mime_multipart['To'] = destinatário
mime_multipart['Subject'] = 'Assunto do e-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso')