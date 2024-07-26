from django.contrib import admin
from .models.models import UserWallet, Crypto, Transaction

admin.site.register(UserWallet)
admin.site.register(Crypto)
admin.site.register(Transaction)
