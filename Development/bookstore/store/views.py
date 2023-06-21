from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Book

from .forms import NameForm

# Create your views here.
def index(request):
    return render(request, 'template.html')

def store(request):
    count = Book.objects.all().count()
    context = {
        'count': count,
    }
    request.session['location'] = "unknown"
    if request.user.is_authenticated:
        request.session['location'] = "Earth"
    return render(request, 'store.html', context)

def login(request):
    return render(request, 'login.html')

def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
        
    else:
        form = NameForm()

    return render(request, "registration_form.html", {"form": form})