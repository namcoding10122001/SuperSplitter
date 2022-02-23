from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import User as CustomUser


#@receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    print('Profile signal triggered')
    if created:
        user = instance
        profile = CustomUser.objects.create(
            user=user,
            email=user.email,
            name=user.first_name,
        )


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=CustomUser)