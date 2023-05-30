from django.contrib import admin
from django.urls import path
from index.views import agendar, inicio, login, home, registro, paciente, doctor, secretaria, reagendar, hora
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="index"),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('home/', home, name="home"),
    path('register/', registro, name="register"),
    path('agendar/', agendar, name="agendar"),
    path('paciente/', paciente, name="paciente"),
    path('doctor/', doctor, name="doctor"),
    path('secretaria/', secretaria, name="secretaria"),
    path('reagendar/', reagendar, name="reagendar"),
    path('hora/', hora, name="hora")
]
