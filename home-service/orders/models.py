from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey('service.Service', on_delete=models.CASCADE)
    adresser = models.CharField(max_length=100)

    def __str__(self) :
        return self.service
