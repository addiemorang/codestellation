from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from OrganizerApp.forms import SignUpForm
from django.views.generic import TemplateView
from django.db.models.signals import post_save
from notifications.signals import notify
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.db import models


class HomePageView(TemplateView):
    template_name = 'home.html'

    def create_group(request):
        if request.method == 'POST':
            form = GroupForm(request.POST)
            if form.is_valid():
                group = form.save()
                group.save()
                return redirect('home')


    # def notify_login():
    #     user = models.ForeignKey(
    #           get_user_model(),
    #           on_delete=models.CASCADE
    #           )
    #     print(type(user))
        #notify.send(User, recipient=User, verb='you have logged in.')

    # notify_login()

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





class SampleView(TemplateView):
    template_name = "index.html"
