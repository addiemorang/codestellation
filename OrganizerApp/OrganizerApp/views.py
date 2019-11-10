from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from OrganizerApp.forms import SignUpForm
from OrganizerApp.forms import GroupForm
from django.views.generic import TemplateView  # Import TemplateView
from django.views.generic.base import TemplateView
from django.contrib.auth import login as auth_login

from django.shortcuts import redirect

from django.http import HttpResponseRedirect

group_names = []

users_groups = {'lw': ['bcj']}

class HomePageView(TemplateView):
    template_name = 'home.html'




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
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

    def update_profile(request, user_id):
        user = User.objects.get(pk=user_id)
        user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
        user.save()

def creategroup(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data.get('group_name')
            description = form.cleaned_data.get('description')
            users_groups[request.user].append(group_name) 
            group_names.append[group_name]
    return render('groups', group_names)
        # #name = request.POST.get('name')
        # form = GroupForm(request.POST)
        # if form.is_valid():
        #     group = form.save()
        #     group.save()
        #     return redirect('home')
        # else:
        #     return redirect('login')


class CalendarView(TemplateView):
    template_name = "calendars.html"
    # if request.method == 'POST':
    #     form = GroupForm(request.POST)
    #     if form.is_valid():

class SampleView(TemplateView):
    template_name = "index.html"


# class ProfileView(TemplateView):
#     template_name = "profile.html"

class GroupView(TemplateView):
    template_name = "group.html"

def profile(request):
    return render(request, 'profile.html')

def login(request):
    return render(request, 'login.html')

def group(request):
    return render(request, 'group.html')


def groups(request):
    return render(request, 'groups.html')
