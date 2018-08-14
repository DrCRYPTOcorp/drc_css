from django.contrib import admin
from .models import Category, Doctor
from doctor import models
# Register your models here.

from .models import User

admin.site.register(models.Category)
admin.site.register(models.Doctor)
# admin.site.register(models.Enterprise)