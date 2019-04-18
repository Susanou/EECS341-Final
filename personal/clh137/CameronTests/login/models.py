from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Role(models.Model):
    MEMBER = 1
    STAFF = 2
    ADMIN = 3

    ROLE_CHOICES = (
        (MEMBER, 'member'),
        (STAFF, 'staff'),
        (ADMIN, 'admin'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key = True)

class User(Abstractuser):
    role = models.ManyToManyField(Role)

