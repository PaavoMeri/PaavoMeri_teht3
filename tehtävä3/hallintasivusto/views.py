from django.shortcuts import render
from .models import Kategoria, Kohde
from datetime import datetime
from .models import SivunLataukset

def index(request):
    kategoriat = Kategoria.objects.all()
    kohteet = Kohde.objects.all()

    today = datetime.now().date()
    today_loads = SivunLataukset.objects.filter(timestamp__date=today).count()

    context = {
        'kategoriat': kategoriat,
        'kohteet': kohteet,
        'today_loads': today_loads,
    }
    return render(request, 'hallintasivusto/index.html', context)
