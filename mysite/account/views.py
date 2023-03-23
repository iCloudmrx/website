from django.shortcuts import render
from .models import Users
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def members(request):
    mymembers=Users.objects.all().values()
    template=loader.get_template('all_members.html')
    context={
        'members':mymembers,
    }
    return HttpResponse(template.render(context,request))