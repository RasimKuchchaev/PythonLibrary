from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path


my_email = EmailMessage()

html_template = Template(Path("templates/index.html").read_text())
html_content = html_template.substitute({'name': 'Rasim', 'date':'tomorrow'})

my_email['from'] = 'Rasim'
my_email['to'] = 'test@mai.ru'
my_email['subject'] = "Let's go out"
# my_email.set_content("Hey! How are you doing?")
my_email.set_content(html_content, 'html')

with open('image/email.gif', 'rb') as img:
    image_data = img.read()
    my_email.add_attachment(image_data, maintype='image', subtype='gif', filename='email.gif')

with smtplib.SMTP(host='127.0.0.1', port='2525') as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print("Email was send")


