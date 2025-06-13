from django.urls import path
from .views import *

urlpatterns=[
    path('index/',Index),
    path('blank/',Blank),
    path('store/',Store),
    path('productdetail/<int:pk>/', ProductDetail.as_view()),
    path('addproduct/',AddProduct),
    path('contact/',Sms),
    path('auth-registration/',Register),
    path('auth-login/',LoginView.as_view()),
    path('logout/',Logout)
]