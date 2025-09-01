from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from .models import Property

# @cache_page(60 * 15)
def property_list(request):
    data = cache.get("property_list")

    if not data:
        properties = Property.objects.all().values('id', 'title', 'description', 'price')
        data = list(properties)
        cache.set("property_list", data, 60 * 15)

    # data = Property.objects.all().values('id', 'title', 'description', 'price')

    return JsonResponse(data, safe=False)
