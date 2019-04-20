""" from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(Abstractuser):
    is_member = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
     """


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    name = models.CharField(max_length = 100)


class Membership(models.Model):
    '''
    Length should be datetime.date value or should it be just an integer?
    '''
    funds = models.IntegerField()
    length = models.IntegerField()
    #length = models.DateField()


class Class(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length=50)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    classes = models.ForeignKey(Class, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

