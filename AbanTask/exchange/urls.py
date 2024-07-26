from django.urls import path
from .views import BuyCryptoView,login_view

urlpatterns = [
    path('buy/', BuyCryptoView.as_view(), name='buy_crypto'),
    path('login/', login_view, name='login'),
]
