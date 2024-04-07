from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import QuoteForm
from .models import Quote, Author

def index(request):
    quotes = Quote.objects.all()
    return render(request, 'index.html', {'quotes': quotes})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': form})









from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quotes.urls')),
]
]
# urls.py (in the main project folder)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quotes.urls')),
]
