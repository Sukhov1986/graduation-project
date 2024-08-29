import requests
from django.conf import settings

from django.core.cache import cache


def currency_rate(request):
    cache_key = 'currency_rate_usd_to_rub'

    rate = cache.get(cache_key)

    if rate is None:
        try:
            response = requests.get(settings.CRYPTO_API_URL, params={
                'ids': 'usd',
                'vs_currencies': 'rub'
            })
            response.raise_for_status()
            data = response.json()
            rate = data.get('usd', {}).get('rub', 'Неизвестно')
        except Exception as e:
            print(f"Ошибка при запросе к API: {e}")
            rate = 'Ошибка'
        cache.set(cache_key, rate, timeout=30)

    return {'currency_rate': rate}
