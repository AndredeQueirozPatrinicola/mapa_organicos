from django.urls import path
from django.contrib.auth import views as auth_views

from accounts import views

urlpatterns = [
    path("", views.accounts),
    path("api/v1/accounts/produtores", views.Produtores.as_view()),

    path("register", views.RegisterView.as_view()),
    path("login", views.LoginView.as_view()),
    path("logout", auth_views.LogoutView.as_view(), name='logout'),
    path("perfil/<id_user>", views.perfil)
]
