from django.shortcuts import render, get_object_or_404

from .models import Category
from .utils import prices, paginate_crypto


def index(request):
    cryptos = prices()
    custom_range, cryptos = paginate_crypto(request, cryptos, 5)

    context = {
        'custom_range': custom_range,
        'cryptos': cryptos
    }

    return render(request, 'crypto/index.html', context)


