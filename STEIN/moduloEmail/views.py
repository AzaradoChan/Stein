import django.http as http
import random
import smtplib
import email.message
from decouple import config
from .models import EmailAnonimo
from mesas.models import Comanda
from django.urls import reverse_lazy

# Create your views here.
def enviar_email(request):
    if request.method == 'GET':
        try:
            e = request.GET['emUser']
        except:
            try:
                cod = request.GET['code']
                ident = request.GET['ident']
            except:
                return http.HttpResponseBadRequest('Informe um Email!!')
            else:
                if ident == '1':
                    contaAnon = EmailAnonimo.objects.filter(codigoUnico=cod)
                    comandas = Comanda.objects.filter(encerrada=False, contaAnon_id=cod)
                    print(len(comandas), len(contaAnon))
                    if len(comandas) > 0 and contaAnon != 1:
                        return http.HttpResponseNotAllowed('Você tem certeza de que já não está com uma comanda aberta?')
                    elif len(contaAnon) == 1:
                        return http.HttpResponse('Autorizado')
                    else:
                        return http.HttpResponseNotAllowed()
                else:
                    contaAnon = EmailAnonimo.objects.filter(codigoUnico=cod)
                    if len(contaAnon) == 1:
                        return http.HttpResponse(reverse_lazy('ver-comandaAnon', kwargs={'codigo_anon': cod}))
                        # return http.HttpResponseRedirect(reverse_lazy('ver-comandaAnon', kwargs={'codigo_anon': cod}))
                    else:
                        return http.HttpResponseNotAllowed()
        else:
            emailAnon = EmailAnonimo.objects.filter(email=e)
            if len(emailAnon) == 0:
                codUnico = ''
                while True:
                    codUnico+=str(random.randrange(0, 10))
                    if len(codUnico) == 6:
                        if len(EmailAnonimo.objects.filter(codigoUnico=codUnico)) != 0:
                            codUnico = ''
                        else:
                            break
                EmailAnonimo.objects.create(
                    email=e,
                    codigoUnico=codUnico)
            
            emailUsuario = e
            cUni = EmailAnonimo.objects.filter(email=e).values()[0]['codigoUnico']

            corpo_email = f"""
            <p>Muito obrigado por escolher nossos serviços!</p>
            <p>Seu código único é: <b> {cUni} </b>
            <p style="color: red"><b>Não o Compartilhe com ninguém!</b></p>"""

            msg = email.message.Message()
            msg['Subject'] = 'Código para Realizar o Pedido'
            msg['From'] = f'{config("EMAIL_HOST_USER")}'
            msg['To'] = f'{emailUsuario}'
            password = config('EMAIL_HOST_PASSWORD')
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(corpo_email)

            s = smtplib.SMTP(f'{config("EMAIL_HOST")}: {config("EMAIL_PORT")}')
            s.starttls()

            s.login(msg['From'], password)
            s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
            return http.HttpResponse()
    else:
        return http.HttpResponseForbidden()