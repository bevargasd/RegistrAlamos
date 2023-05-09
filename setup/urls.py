from django.contrib import admin
from django.urls import path
from index.views import inicio, login, home, registro
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="index"),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('home/', home, name="home"),
    path('register/', registro, name="register")
]
