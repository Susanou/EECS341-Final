from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from login.models import Member

# Create your views here.

#testing directing to url
def index(request):
    try:
        # need to adjust given input
        member = Member.objects.get(name='Melody')
    except Member.DoesNotExist:
        raise Http404("no such member")
    print(member)
    context = {
        'Display the member name' : member.name, 
    }
    return render(request, 'profile/index.html', context)
