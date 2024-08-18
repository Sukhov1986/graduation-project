import requests
from django.conf import settings


def currency_rate(request):
    try:
        response = requests.get(settings.CRYPTO_API_URL, params={
            'ids': 'usd',
            'vs_currencies': 'rub'
        })
        data = response.json()
        rate = data.get('usd', {}).get('rub', 'Неизвестно')
    except Exception as e:
        rate = 'Ошибка'
    return {'currency_rate': rate}
