from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from .models import Member

# Create your views here.
def members(request):
    mymembers=Member.objects.all().values()
    template=loader.get_template('members/all_members.html')
    context={
        'users':mymembers,
    }
    return HttpResponse(template.render(context,request))


def login(request):
    return render(request,'members/login.html')

def register(request):
    if request.method=='POST':
        username=request.Post['username']
        email=request.Post['email']
        password=request.Post['password']
        user=Member(username=username,email=email,password=password)
        user.save()
        return redirect('/')
    else:
        return render(request,'members/login.html')