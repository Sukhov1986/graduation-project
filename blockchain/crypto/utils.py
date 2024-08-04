import requests
from django.conf import settings
from .models import Crypto
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def prices():
    cryptos = Crypto.objects.all()

    crypto_ids = ','.join([crypto.name.lower() for crypto in cryptos])

    api_url = f"{settings.CRYPTO_API_URL}?ids={crypto_ids}&vs_currencies=usd"
    response = requests.get(api_url)
    data = response.json()

    for crypto in cryptos:
        price = data.get(crypto.name.lower(), {}).get('usd', 'Не доступно')

        crypto.price = price

    sorted_cryptos = sorted(cryptos, key=lambda c: float(c.price) if c.price != 'Не доступно' else float('inf'),
                            reverse=True)
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
