from django.urls import path
from .import views

urlpatterns =[
    path('register/',views.Register.as_view(),name='register'),
    path('login/',views.login,name='login'),
]