from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_list, name="property-list"),
    path('cache-metrics/', views.cache_metrics_view, name='cache_metrics'),
]