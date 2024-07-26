from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ...models.models import Crypto, UserWallet


class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        cryptos = [
            {'name': 'Bitcoin', 'current_price_usd': 30000.0},
            {'name': 'Ethereum', 'current_price_usd': 2000.0},
            {'name': 'Ripple', 'current_price_usd': 0.5},
            {'name': 'USDT', 'current_price_usd': 1.0}
        ]
        for crypto_data in cryptos:
            Crypto.objects.update_or_create(name=crypto_data['name'], defaults=crypto_data)

        default_user, created = User.objects.update_or_create(username='testuser',
                                                              defaults={'password': 'testtest123'})

        usdt = Crypto.objects.get(name='USDT')
        UserWallet.objects.update_or_create(user=default_user, crypto=usdt, defaults={'amount': 10000.0})

        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))
