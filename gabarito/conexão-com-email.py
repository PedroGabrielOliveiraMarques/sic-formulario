import smtplib
import email.message
def enviar_email():
    corpo_email="""
    <p>ola mundo<p>
    """
    msg = email.message.Message()
    msg['subject'] = "assunto"
    msg['from'] = 'pg100526@gmail.com'
    msg['To'] = 'pg10052600@gmail.com'
    password= 'qmngdoeghcmzkhjh'
    msg.add_header('Content-type','text/html')
    msg.set_payload(corpo_email)

    s= smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # login 
    s.login(msg['From'],password)
    s.sendmail(msg['From'],[msg['To']],msg.as_string().encode('utf-8'))
    print('email enviado com sucesso')
enviar_email()
    