from django.db import models
from django.db.models.enums import IntegerChoices
from django.db.models.fields.files import ImageField
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    category = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name="parent_cat")
    image = ImageField()

    def __str__(self) :
        return self.category

class Service(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="cat")
    image = models.ImageField()
    detail = models.TextField()
    price  = models.DecimalField(decimal_places=2, max_digits=2)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    comment = models.TextField()