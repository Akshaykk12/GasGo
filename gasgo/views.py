from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
 
# Views
@login_required
def home(request):
    return render(request, "registration/success.html", {})
 
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return render(request, "registration/success.html", {})
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def userDetails(request, username):
    data = {
        'name':username
    }
    return render(request, 'accounts/account_overview.html',data)

@login_required
def account_overview(request):
    return render(request, 'accounts/account_overview.html')