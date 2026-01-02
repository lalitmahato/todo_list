from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
import time
from users.models import CustomUser


@receiver(pre_save, sender=CustomUser)
def user_pre_save(sender, instance, **kwargs):
    # You can do certain action here...
    print("Pre save action started...")
    print(f"[PRE_SAVE] User about to be saved: {instance.username}")


@receiver(post_save, sender=CustomUser)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"[POST_SAVE] New user created: {instance.username}")
    else:
        print(f"[POST_SAVE] User updated: {instance.username}")


@receiver(pre_delete, sender=CustomUser)
def user_pre_delete(sender, instance, **kwargs):
    print(f"[PRE_DELETE] User about to be deleted: {instance.username}")


@receiver(post_delete, sender=CustomUser)
def user_post_delete(sender, instance, **kwargs):
    print(f"[POST_DELETE] User deleted: {instance.username}")
