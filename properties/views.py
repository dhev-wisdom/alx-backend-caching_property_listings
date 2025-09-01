from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from .models import Property
from .utils import get_all_properties, get_redis_cache_metrics

# @cache_page(60 * 15)
def property_list(request):
    data = get_all_properties()
    return JsonResponse(data, safe=False)

def cache_metrics_view(request):
    metrics = get_redis_cache_metrics()
    return JsonResponse(metrics)
