from django.db import models

class Kategoria(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Kategoriat"

class Kohde(models.Model):
    category = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True)
    link = models.URLField(blank=True)
    credentials = models.CharField(max_length=200, blank=True)
    class Meta:
        verbose_name_plural = "Kohteet"

class SivunLataukset(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    class Meta:
        verbose_name_plural = "Sivun Lataukset"



class UserType(models.Model):
    type_name = models.CharField(max_length=50)



