from django.shortcuts import render
from .models import *

def index_view(request):
    soz = request.GET.get('soz')
    if soz is not None:
        soz = soz.lower()
        togrilar = Togri.objects.filter(soz=soz)
        if togrilar.exists():
            togri = togrilar.first()
            notogrilar = Notogri.objects.filter(togri=togri)
    return render(request, 'index.html')
