from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from login.models import Member, Class, Staff, MemberLevel

# Create your views here.

#testing directing to url
def index(request):
    try:
        # need to adjust given input
        mname = 'GenTsuki'
        #using raw sql
        member = Member.objects.raw('SELECT * FROM login_member m WHERE m.name = %s', [mname])[0]
        classes = Class.objects.raw('SELECT c.id, c.name, c.location, c.staff_id FROM login_class c, login_member m WHERE m.name = %s AND m.classes_id = c.id', [mname])
        level = MemberLevel.objects.raw('SELECT l.level_status, l.price FROM login_memberlevel l, login_member m WHERE m.name = %s AND m.level_id = l.level_status', [mname])[0]
    except Member.DoesNotExist:
        raise Http404("no such member")
    print(member)
    context = {
        'member' : member,
        'classes': classes,
        'level': level,
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