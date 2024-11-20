from .forms import ReservationForm
from django.shortcuts import render, redirect
# Create your views here.
def book(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ReservationForm()
    return render(request, 'book.html', {'form': form})

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def specials(request):
    return render(request, 'specials.html')

def events(request):
    return render(request, 'events.html')

def chefs(request):
    return render(request, 'chefs.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

def success(request):
    return render(request, 'success.html')
