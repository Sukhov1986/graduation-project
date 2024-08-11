from django.shortcuts import render, get_object_or_404

from .models import Category, Crypto
from .utils import prices, paginate_crypto


def index(request, category_id=None):
    if category_id:
        selected_category = get_object_or_404(Category, id=category_id)
        cryptos = Crypto.objects.filter(categories=selected_category)
    else:
        selected_category = None
        cryptos = Crypto.objects.all()

    cryptos = prices(cryptos)

    custom_range, cryptos = paginate_crypto(request, cryptos, 5)

    categories = Category.objects.all()

    context = {
        'categories': categories,
        'custom_range': custom_range,
        'cryptos': cryptos,
        'selected_category': selected_category,
    }

    return render(request, 'crypto/index.html', context)


