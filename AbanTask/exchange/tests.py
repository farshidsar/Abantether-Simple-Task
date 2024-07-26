from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from AbanTask.exchange.models.models import Crypto, UserWallet

class ExchangeTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testtest123')
        self.client.login(username='testuser', password='testtest123')

        self.crypto = Crypto.objects.create(name='Bitcoin', current_price_usd=50000)
        self.cryptoUSDT = Crypto.objects.create(name='USDT', current_price_usd=1)
        self.user_wallet = UserWallet.objects.create(user=self.user, crypto=self.cryptoUSDT, amount=100000000000)

    def test_buy_crypto(self):
        data = {
            'crypto_name': 'Bitcoin',
            'amount': 12
        }
        response = self.client.post(reverse('buy_crypto'), data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('success' in response.data)
        self.assertTrue(response.data['success'])
