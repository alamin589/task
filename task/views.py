# views.py
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from .forms import SocialMediaFormSet
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserProfileForm
from .models import UserProfile

def socialmediaview(request):
    user_profile = None
    if request.method == 'POST':
        formset = SocialMediaFormSet(request.POST)
        if formset.is_valid():
            user_profile_id = request.POST.get('user_profile_id')
            user_profile = UserProfile.objects.get(id=user_profile_id)

            for form in formset:
                if form.is_valid():
                    social_media_account = form.save(commit=False)
                    social_media_account.user_profile = user_profile
                    social_media_account.save()
            return redirect('userprofile_list')
    else:
        formset = SocialMediaFormSet()
    return render(request, 'social.html', {'formset': formset, 'user_profile': user_profile})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userprofile_list')  # Redirect to registration success page
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def userprofile_list(request):
    userprofiles = UserProfile.objects.all()
    return render(request, 'userprofile_list.html', {'userprofiles': userprofiles})

def userprofile_create(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userprofile_list')
    else:
        form = UserProfileForm()
    return render(request, 'user_create_update.html', {'form': form})

def userprofile_update(request, pk):
    userprofile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=userprofile)
        if form.is_valid():
            form.save()
            return redirect('userprofile_list')
    else:
        form = UserProfileForm(instance=userprofile)
    return render(request, 'user_create_update.html', {'form': form})

def userprofile_delete(request, pk):
    userprofile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        userprofile.delete()
        return redirect('userprofile_list')
    return render(request, 'user_delete.html', {'userprofile': userprofile})
