from django.http import HttpResponse
from django.shortcuts import render
from .models import Produkty, Kategoria, Zdj


# Create your views here.

def index(request):
    wszystkie = Produkty.objects.all()
    jeden = Produkty.objects.get(pk=2)
    kategorie = Kategoria.objects.all()
    dane = {'kategorie': kategorie}
    return render(request, 'szablon.html', dane)


def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_produkt = Produkty.objects.filter(kategoria = kategoria_user)
    kategorie = Kategoria.objects.all()
    dane = { 'kategoria_user': kategoria_user,
             'kategoria_produkt': kategoria_produkt,
             'kategorie': kategorie }
    return render(request, 'kategoria_produkt.html', dane)


def produkt(request, id):
    kategorie = Kategoria.objects.all()
    produkt_user = Produkty.objects.get(pk=id)
    dane = {'produkt_user': produkt_user, 'kategorie': kategorie}
    return render(request, 'produkt.html', dane)


def zdj(request, id):
    kategorie = Kategoria.objects.all()
    zdjecie_user = Zdj.objects.get(pk=id)
    dane = {'zdjecie_user': zdjecie_user, 'kategorie': kategorie}
    return render(request, 'produkt.html', dane)