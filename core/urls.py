from django.contrib import admin
from django.urls import path,include
from core import views
app_name = 'core'

urlpatterns = [
    # path('Me/',views.Me.as_view(), name="Me"),
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('user/', views.UserView.as_view()),
    path('logout/',  views.LogoutView.as_view()),
]