from django.shortcuts import render
from django.http import HttpResponse
from . models import Product
from math import ceil

def home(request):
    products= Product.objects.all()
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}

    return render(request, 'home.html', params)
# def about(request):
#     return HttpResponse("<h1>About Page</h1><br><a href='/'>Home</a>")
def about(request):
    return render(request, 'about.html')
def form(request):
    return render(request, 'form.html')


def formAction(request):
    fname = request.POST.get('fname', '')
    lname = request.POST.get('lname', '')
    params = {'fname':fname, 'lname':lname}
    return render(request, 'form_data.html', params)