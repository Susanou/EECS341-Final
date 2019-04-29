from django.urls import path

from . import views

app_name = 'profile'

urlpatterns = [
    # "/polls" is the prefix
    path('', views.index, name='index'),
    path('<int:class_id>/class/', views.classInfo, name='class'),
    path('classlist', views.classlist, name='classlist'),
    path('staff', views.staff, name='staff'),
]
