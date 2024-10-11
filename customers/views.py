
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, CustomerProfileUpdateForm


@login_required
def account_overview(request):
    return render(request, 'accounts/account_overview.html')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = CustomerProfileUpdateForm(request.POST, request.FILES, instance=request.user.customerprofile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = CustomerProfileUpdateForm(instance=request.user.customerprofile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(request, 'customers/profile.html', context)
