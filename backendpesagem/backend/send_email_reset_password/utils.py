import random
from django.core.mail import send_mail
from django.conf import settings
from .models import VerificationCode
from datetime import timedelta
from django.utils import timezone

def send_verification_email(email):
    code = random.randint(100000, 999999)  # gera cod  de 6 dígitos
    expires_at = timezone.now() + timedelta(minutes=15)

    # armazenar o cod no banco de dados
    VerificationCode.objects.create(email=email, code=str(code), expires_at=expires_at)

    # envia o e-mail
    subject = 'Código de Verificação'
    message = f'Seu código de verificação é: {code}'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

    return str(code)  # Retorna o cod para debug 
