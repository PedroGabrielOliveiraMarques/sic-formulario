import smtplib
import email.message
from flask import Flask, render_template,redirect,request

app= Flask(__name__ ,template_folder='template', static_folder='static')

@app.route("/")
def home():
    
    return render_template ("home.html")
#separação 
@app.route("/formulario",methods=['POST','GET'])
def enviar_email():
    emailhtml= request.form.get('nome')
    corpo_email=emailhtml
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
    print ('o email "'+emailhtml+'" foi enviado para a caixa de email')
    
    return redirect("/")
if __name__ =="__main__":
    app.run(debug=True)