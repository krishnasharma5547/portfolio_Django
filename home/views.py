from django.shortcuts import render

from home.models import contact


# Create your views here.
def home(request):
    # return HttpResponse('hii i am home')
    return render(request, 'home.html')


def projects(request):
    return render(request, 'projects.html')


def contacts(request):
    if request.method == 'POST':
        print('this is POST')
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        ins = contact(name=name, phone=phone, email=email, message=message)
        ins.save()
        print('done')
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
