from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.db import connection
from django.db.models import Count
from login.models import Member, Class, Staff, MemberLevel

# Create your views here.

#testing directing to url
def index(request):
    try:
        # need to adjust given input
        mname = 'Melody'
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
    class_object = Class.objects.raw('SELECT * FROM login_class c WHERE c.id = %s', [class_id])[0]
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(DISTINCT id) FROM login_member_classes WHERE login_member_classes.class_id = %s", [class_id])
        row = cursor.fetchone()
        student_num = row[0]
    context = {
        'class': class_object,
        'number': student_num
    }
    return render(request, 'profile/class.html', context)

def classlist(request):
    classlist = Class.objects.raw('SELECT * FROM login_class')
    context = {
        'classlist': classlist,
    }
    return render (request, 'profile/classlist.html',context)

# implement raw sql query later on
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