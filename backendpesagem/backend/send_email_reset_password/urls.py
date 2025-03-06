from django.urls import path
from . import views

urlpatterns = [
    path('send-reset-password/', views.send_email_view, name='send-reset-password'),
    path('verify-reset-password/', views.verify_code_view, name='verify-reset-password'),
]
