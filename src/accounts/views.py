from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate , login
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from .models import Profile
from .forms import UserForm, ProfileForm
# Create your views here.
def home(request):
    pass




def register(request):
    if request.method == 'POST':  # meaning when i click sigup
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, pasword=password)
            login(request,user)
            print(request.user)
            return redirect('/notes')
    else:
         form = UserCreationForm
    context = {
            'form': form,
        }

    return render(request, 'signup.html', context)



def profile(request,slug):
    profile = get_object_or_404(Profile,slug=slug)
    context = {
        'profile':profile,
    }

    return render(request,'profile.html',context)


def edit_profile(request, slug):
    profile = get_object_or_404(Profile,slug=slug) # to call the user
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES,instance=profile)
        if user_form.is_valid() and profile_form.is_valid() :
            user_form.save()
            new_profile = profile_form.save()
            return redirect('/notes')




    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form

    }
    return render(request,'edit_profile.html',context)



def change_password(request,slug):
    profile = get_object_or_404(Profile, slug=slug)
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            password_form.save()
            return redirect('/notes')
    else:
        password_form = PasswordChangeForm(request.user)
    context = {
        'password_form': password_form
    }

    return render(request,'change_password.html',context)
