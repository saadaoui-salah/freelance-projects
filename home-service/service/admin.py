from django.contrib import admin
from .models import Service, Review, Category

admin.site.register(Service)
admin.site.register(Review)
admin.site.register(Category)