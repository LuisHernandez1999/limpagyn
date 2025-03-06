from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import VerificationCode
from .utils import send_verification_email

@api_view(['POST'])
def send_email_view(request):
    email = request.data.get('email')
    if not email:
        return Response({'error': 'O campo email é obrigatório'}, status=400)

    code = send_verification_email(email)
    return Response({'message': 'Código enviado com sucesso', 'code': code})

@api_view(['POST'])
def verify_code_view(request):
    email = request.data.get('email')
    code = request.data.get('code')

    if not email or not code:
        return Response({'error': 'E-mail e código são obrigatórios'}, status=400)

    try:
        verification_code = VerificationCode.objects.filter(email=email, code=code).latest('created_at')
    except VerificationCode.DoesNotExist:
        return Response({'error': 'Código de verificação inválido ou não encontrado'}, status=400)

    if verification_code.is_expired():
        return Response({'error': 'Código expirado'}, status=400)

    return Response({'message': 'Código verificado com sucesso!'}, status=200)
