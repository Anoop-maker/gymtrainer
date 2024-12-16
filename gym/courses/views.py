from django.shortcuts import render, redirect

from shop.models import Users


# Create your views here.


def about(request):
    return render(request,'about.html')

def courses(request):
    return render(request,'courses.html')

def login(request):
    if request.method=='POST':

        e = request.POST['e']
        p1 = request.POST['p1']


        u = Users.objects.create_user(email=e, password=p1,)
        u.save()
        return redirect('courses:login')

    return render(request,'login.html')
