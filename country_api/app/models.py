from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    cca2 = models.CharField(max_length=2, unique=True)
    capital = models.CharField(max_length=100, blank=True)
    population = models.BigIntegerField()
    area = models.FloatField()
    flag_url = models.URLField() 
    timezones = models.JSONField()

    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='countries')
    languages = models.ManyToManyField(Language, related_name='countries')
    
    borders = models.JSONField(default=list)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Countries"