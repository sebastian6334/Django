from django.db import models


class Zdj(models.Model):
    def __str__(self):
        return self.zdjecie

    przedmiot = models.TextField(blank=True)
    zdjecie = models.TextField(blank=True)

    class Meta:
        verbose_name = "Zdjęcie"
        verbose_name_plural = "Zdjęcia"


class Producent(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=60)
    opis = models.TextField(blank=True)

    class Meta:
        verbose_name = "Producent"
        verbose_name_plural = "Producenci"


class Kategoria(models.Model):


    nazwa = models.CharField(max_length=30)
    rodzaj_parametrow1 = models.TextField(blank=True)
    rodzaj_parametrow2 = models.TextField(blank=True)
    rodzaj_parametrow3 = models.TextField(blank=True)
    rodzaj_parametrow4 = models.TextField(blank=True)

    def __str__(self):
        return self.nazwa
    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"


class Wartosc(models.Model):
    # nazwa = models.ForeignKey(Kategoria, null=True, blank=True, on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=40)
    wartosc_parametrow1 = models.TextField(blank=True)
    wartosc_parametrow2 = models.TextField(blank=True)
    wartosc_parametrow3 = models.TextField(blank=True)
    wartosc_parametrow4 = models.TextField(blank=True)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Wartość parametru"
        verbose_name_plural = "Wartości parametrów"

class Produkty(models.Model):
    kategoria = models.ForeignKey(Kategoria, null=True, blank=True, on_delete=models.CASCADE)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE, null=True)
    nazwa = models.CharField(max_length=100)
    opis_1 = models.TextField(blank=True)
    opis_2 = models.TextField(blank=True)
    opis_3 = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=12, decimal_places=2)
    zdjecie = models.ForeignKey(Zdj, null=True, blank=True, on_delete=models.CASCADE)
    wartosc = models.ForeignKey(Wartosc, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"


