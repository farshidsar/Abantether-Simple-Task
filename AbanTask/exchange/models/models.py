from django.db import models
from django.contrib.auth.models import User

class Crypto(models.Model):
    name = models.CharField(max_length=100, unique=True)
    current_price_usd = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name

class UserWallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=8)

    def __str__(self):
        return f"{self.user.username} - {self.crypto.name}"

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    is_world_trade = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.crypto.name} - {self.amount}"
