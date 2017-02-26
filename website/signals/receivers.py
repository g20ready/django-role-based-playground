from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

from rolepermissions.shortcuts import assign_role

@receiver(post_save, sender=User, dispatch_uid="user_pre_save_roles")
def user_pre_save(sender, **kwargs):
    #sender is a user object
    user = kwargs.pop('instance')
    assign_role(user, 'visitor')
    print("visitor role assigned")