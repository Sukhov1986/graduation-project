import requests
from django.shortcuts import render
from .models import Crypto
from django.conf import settings


def index(request):
    cryptos = Crypto.objects.all()
    crypto_ids = ','.join([crypto.name for crypto in cryptos])
    api_url = f"{settings.CRYPTO_API_URL}?ids={crypto_ids}&vs_currencies=usd"
    response = requests.get(api_url)
    data = response.json()
    context = {
        'crypto_prices': {crypto.name: data.get(crypto.name, {}).get('usd', 'N/A') for crypto in cryptos}
    }
    return render(request, 'crypto/index.html', context)

# Create your views here.
