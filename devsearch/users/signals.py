from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save
from .models import Profile


def make_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(user=user, username=user.username, email=user.email, name=user.first_name)


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(make_profile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(delete_user, sender=Profile)
