from django.db import models
from django.contrib.auth.models import User  

class VerificationCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    email = models.EmailField()
    code = models.CharField(max_length=50)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"Verification code for {self.email}"
