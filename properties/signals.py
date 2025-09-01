from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Property

# Invalidate cache when a Property is created or updated
@receiver(post_save, sender=Property)
def invalidate_all_properties_cache_on_save(sender, instance, **kwargs):
    print("Property saved – clearing 'all_properties' cache")
    cache.delete('all_properties')

# Invalidate cache when a Property is deleted
@receiver(post_delete, sender=Property)
def invalidate_all_properties_cache_on_delete(sender, instance, **kwargs):
    print("Property deleted – clearing 'all_properties' cache")
    cache.delete('all_properties')
