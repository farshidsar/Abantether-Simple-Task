from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models.models import Crypto, UserWallet, Transaction
from .services.transaction_service import TransactionService
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import json


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login successful"})
        else:
            return JsonResponse({"message": "Invalid credentials"}, status=401)
    return JsonResponse({"message": "Method not allowed"}, status=405)



class BuyCryptoView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        crypto_name = request.data.get('crypto_name')
        amount = float(request.data.get('amount'))

        try:
            crypto = Crypto.objects.get(name=crypto_name)
        except Crypto.DoesNotExist:
            return Response({'error': 'Crypto not found'}, status=status.HTTP_404_NOT_FOUND)

        transaction_service = TransactionService()
        result = transaction_service.buy_crypto(user_id, crypto, amount)

        if result['success']:
            return Response({'success': True, 'message': result['message']}, status=status.HTTP_201_CREATED)
        else:
            return Response({'success': False, 'message': result['message']}, status=status.HTTP_400_BAD_REQUEST)




