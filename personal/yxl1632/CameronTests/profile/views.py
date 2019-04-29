from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from login.models import Member, Class, Staff

# Create your views here.

#testing directing to url
def index(request):
    try:
        # need to adjust given input
        member = Member.objects.get(name='Melody')
        classes = member.classes.all()
    except Member.DoesNotExist:
        raise Http404("no such member")
    print(member)
    context = {
        'member' : member,
        'classes': classes,
    }
    return render(request, 'profile/index.html', context)

def classInfo(request, class_id):
    class_object = get_object_or_404(Class, pk=class_id)
    return render(request,'profile/class.html',{'class':class_object})

def classlist(request):
    classlist = Class.objects.all()
    context = {
        'classlist': classlist,
    }
    return render (request, 'profile/classlist.html',context)

def staff(request):
    try:
        # need to adjust given input
        staff = Staff.objects.get(name='Melody')
        classes = Class.objects.filter(staff=staff)
    except Class.DoesNotExist:
        raise Http404("no such member")
    context = {
        'staff' : staff,
        'classes': classes,
    }
    return render(request, 'profile/staff.html', context)
