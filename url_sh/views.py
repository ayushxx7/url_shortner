from django.shortcuts import render, redirect
from .models import short_urls
from .forms import UrlForm
from .shortner import shortner

# Create your views here.

def Home(request, token):
    urls = short_urls.objects.all()
    print(urls.values())
    for i in urls:
        print(i)
    long_url = short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)

def Make(request):
    form = UrlForm(request.POST)
    token = ""
    if request.method == "POST":
        if form.is_valid():
            NewUrl = form.save(commit=False)
            token = shortner().issue_token()
            token_list = [key['short_url'] for key in short_urls.objects.values()]
            while token in token_list:
                token = shortner().issue_token()
            NewUrl.short_url = token
            NewUrl.save()
        else:
            form = UrlForm()
            token = "Invalid URL"
    return render(request, 'home.html', {'form': form, 'token': token})
