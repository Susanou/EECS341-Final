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
from datetime import time

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    name = models.CharField(max_length = 100)

class MemberLevel(models.Model):
    name = (
        ('B', 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold'),
        ('P', 'Platinum'),
        ('D', 'Diamond'), 
    )
    level_status = models.CharField(max_length=1, choices=name, default='B', primary_key=True)
    price = models.IntegerField()

class Class(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length=50)
    day_options = (
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    )
    time_day = models.CharField(max_length=3, choices=day_options, default='WED')
    time_start = models.TimeField(default=time(15, 30, 0)) #default start time is 15:30:00, use print() to retrieve later on
    time_end = models.TimeField(default=time(16, 30, 0))
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    classes = models.ManyToManyField(Class)
    level = models.ForeignKey(MemberLevel, default='B', on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

class Membership(models.Model):
    '''
    Length should be datetime.date value or should it be just an integer?
    '''
    funds = models.IntegerField()
    length = models.IntegerField()
    #length = models.DateField()

