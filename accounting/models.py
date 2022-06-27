from django.db import models
from django.contrib.auth.models import User


class CustomUserModel(models.Model):
    GENDERS = (
        ('F', 'female'),
        ('M', 'male'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    national_code = models.CharField(max_length=10, null=True, blank=True)
    debt = models.OneToOneField("loan.DebtModel", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'
