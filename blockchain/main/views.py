

from django.shortcuts import render, get_object_or_404
from .models import CryptoPerson


def home(request):
    people = CryptoPerson.objects.all()
    context = {'people': people}
    return render(request, 'main/home.html', context)


def person_detail(request, person_id):
    person = get_object_or_404(CryptoPerson, id=person_id)
    context = {
        'person': person,
    }
    return render(request,'main/person_detail.html', context)
