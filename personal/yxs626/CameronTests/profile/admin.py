from django.contrib import admin

# Register your models here.

from login.models import Member, Staff, Class

admin.site.register(Member)
admin.site.register(Staff)
admin.site.register(Class)