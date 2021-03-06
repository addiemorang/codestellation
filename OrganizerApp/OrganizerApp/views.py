from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from OrganizerApp.forms import SignUpForm
from OrganizerApp.forms import GroupForm, DocForm
from django.views.generic import TemplateView  # Import TemplateView
from django.views.generic.base import TemplateView
from django.contrib.auth import login as auth_login
from OrganizerApp.Backend.analyze_agenda import main as analyze

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
    # list = [['Email Prof. Antonella', '@amorang', '11/30/19'],
    #         ['Print out flyers', '@lwingard', '11/26/19'],
    #         ['Create agenda', '@ellie', '11/20/19'],
    #         ]
    # action1 = render(request, 'actionitem.html', {'desciption': list[0][0], 'assignee': list[0][1], 'date': list[0][2]})
    # action2 = render(request, 'actionitem.html', {'desciption': list[1][0], 'assignee': list[1][1], 'date': list[1][2]})
    # action3 = render(request, 'actionitem.html', {'desciption': list[2][0], 'assignee': list[2][1], 'date': list[2][2]})
    #
    #
    # return render(request, group.html, {'action1': action1,'action2': action2,'action3': action3})
    template_name = "group.html"

    def req_analyze(request):
        if request.method == 'POST':
            form = DocForm(request.POST)
            if form.is_valid():
                analyze(request.document_id)

            else:
                group

def profile(request):
    return render(request, 'profile.html')

def login(request):
    return render(request, 'login.html')

def group(request):
    return render(request, 'group.html')


def groups(request):
    return render(request, 'groups.html')
