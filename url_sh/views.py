from django.shortcuts import render
from .models import short_urls
from .forms import UrlForm
from .shortner import shortner

# Create your views here.
def Make(request):
    form = UrlForm(request.POST)
    token = ""
    if request.method == "POST":
        if form.is_valid():
            NewUrl = form.save(commit=False)
            token = shortner().issue_token()
            NewUrl.save()
        else:
            form = UrlForm()
            token = "Invalid URL"
    return render(request, 'home.html', {'form': form, 'token': token})
