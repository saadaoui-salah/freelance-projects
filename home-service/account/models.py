from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=30)
    family_name = models.CharField(max_length=30)
    phone = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.name+' '+self.family_name