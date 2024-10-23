from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from .models import Car

@receiver(signal=pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    print("### PRE SAVE ###")