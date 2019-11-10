from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from OrganizerApp.forms import SignUpForm
from django.views.generic import TemplateView  # Import TemplateView
from django.views.generic.base import TemplateView

from django.shortcuts import redirect

from django.http import HttpResponseRedirect


class HomePageView(TemplateView):
    template_name = 'home.html'

    def create_group(request):
        if request.method == 'POST':
            form = GroupForm(request.POST)
            if form.is_valid():
                group = form.save()
                group.save()
                return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

    def update_profile(request, user_id):
        user = User.objects.get(pk=user_id)
        user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
        user.save()


# def profile(request):
#     return redirect('profile.html')

class SampleView(TemplateView):
    template_name = "index.html"


class ProfileView(TemplateView):
    template_name = "profile.html"
