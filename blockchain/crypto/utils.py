import requests
from django.conf import settings
from .models import Crypto
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.cache import cache


def get_crypto_prices(crypto_ids):
    api_url = f"{settings.CRYPTO_API_URL}?ids={crypto_ids}&vs_currencies=usd"
    cache_key = f"crypto_prices_{crypto_ids}"
    data = cache.get(cache_key)

    if data is None:
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Проверка на ошибки HTTP
            data = response.json()
            cache.set(cache_key, data, timeout=30)
        except requests.RequestException as e:
            print(f"Ошибка при запросе к API: {e}")
            data = cache.get(cache_key)

    return data


def prices(cryptos):

    crypto_ids = ','.join([crypto.name.lower() for crypto in cryptos])
    data = get_crypto_prices(crypto_ids)

    if not data:
        return cryptos
    for crypto in cryptos:
        price = data.get(crypto.name.lower(), {}).get('usd', 'Не доступно')
        crypto.price = price

    sorted_cryptos = sorted(
        cryptos,
        key=lambda c: float(c.price) if c.price != 'Не доступно' else float('inf'),
        reverse=True
    )

    return sorted_cryptos


def paginate_crypto(request, cryptos, result):
    page = request.GET.get('page', 1)
    paginator = Paginator(cryptos, result)
    try:
        cryptos = paginator.page(page)
    except PageNotAnInteger:
        cryptos = paginator.page(1)
    except EmptyPage:
        cryptos = paginator.page(paginator.num_pages)
    current_page = int(page)
    left_index = max(current_page - 3, 1)
    right_index = min(current_page + 4,
                      paginator.num_pages + 1)
    custom_range = range(left_index, right_index)
    return custom_range, cryptos
