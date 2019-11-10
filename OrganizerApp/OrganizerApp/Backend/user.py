from django.db.models.signals import post_save
from notifications.signals import notify
from OrganizerApp.models import Profile

def getGroups(user):
    return request.user.groups


def addToGroup(user, group):
    group = Group.objects.get(name=group)
    group.user_set.add(your_user)
