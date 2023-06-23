from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Book

from .forms import NameForm

# Create your views here.
def index(request):
    return render(request, 'template.html')

def store(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'store.html', context)

def book_details(request, book_id):
    context = {
        'book': Book.objects.get(pk=book_id),
    }
    return render(request, 'store/detail.html', context)

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