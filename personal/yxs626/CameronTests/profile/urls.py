from django.urls import path

from . import views

app_name = 'profile'

urlpatterns = [
    # "/polls" is the prefix
    path('', views.index, name='index'),

]
