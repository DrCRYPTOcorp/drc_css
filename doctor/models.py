from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_category')
    sort = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return '{} {}'.format(self.sort, self.user)


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_doctor')
    name = models.CharField(max_length=30, blank=False)
    medical_name = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=200, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    license_number = models.IntegerField(blank=False)
    certification = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


# class Enterprise(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enterprise_user')
#     enterprise_name = models.CharField(max_length=20, blank=True)
#     enterprise_category = models.CharField(max_length=30, blank=True)
#     uploaded_at = models.DateTimeField(auto_now_add=True)

