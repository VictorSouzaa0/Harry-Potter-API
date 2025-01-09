from django.db import models

class Spell(models.Model):
    name = models.CharField(max_length=200) # campo de texo com limitação
    description = models.TextField() # campo de texto sem limtação

    def __str__(self):
        return self.name
    
class Charcaters(models.Model):
    name = models.CharField(max_length=200)
    house = models.CharField(max_length=200)
    wizard = models.BooleanField()
    eyeColor = models.CharField(max_length=200)
    hairColor = models.CharField(max_length=200)
    actor = models.CharField(max_length=200)
    image = models.TextField()