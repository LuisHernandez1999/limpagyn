from django.urls import path
from .views import CreateView, LoginView

urlpatterns = [
    path("create/", CreateView.as_view(), name="create"),
    path("login/", LoginView.as_view(), name="login"),
]
