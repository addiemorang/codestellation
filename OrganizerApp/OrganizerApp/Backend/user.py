from django.contrib.auth.models import Group


def getGroups(user):
    return request.user.groups


def addToGroup(user, group):
    group = Group.objects.get(name=group)
    group.user_set.add(your_user)
