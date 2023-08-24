from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
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