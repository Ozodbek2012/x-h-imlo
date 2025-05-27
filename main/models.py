from django.db import models

class Togri(models.Model):
    soz = models.CharField(max_length=50)

    def __str__(self):
        return self.soz

    class Meta:
        verbose_name_plural = "Togri so'zlar"

class Notogri(models.Model):
    soz = models.CharField(max_length=50)
    togri = models.ForeignKey(Togri, on_delete=models.CASCADE)

    def __str__(self):
        return self.soz

    class Meta:
        verbose_name_plural = "Notogri so'zlar"


