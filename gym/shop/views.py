from django.contrib import messages
from shop.models import Users
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request,'home.html')

def pricing(request):
    return render(request,'price.html')





def signin(request):
    if request.method=='POST':
        un=request.POST['un']
        fn = request.POST['fn']
        ln = request.POST['ln']
        p = request.POST['p']
        e = request.POST['e']
        p1 = request.POST['p1']
        p2 = request.POST['p2']

        u = Users.objects.create(username=un, password=p1, firstname=fn, lastname=ln, email=e, conformpassword=p2,
                                               phone=p,)
        u.save()
        return redirect('courses:login')

    return render(request, 'signin.html', )






