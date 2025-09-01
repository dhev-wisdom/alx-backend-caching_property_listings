from django.core.cache import cache
from .models import Property
from django_redis import get_redis_connection
import logging

logger = logging.getLogger(__name__)

def get_all_properties():
    queryset = cache.get("all_properties")

    if queryset is None:
        print("fetching properties from DB...")
        properties_qs = Property.objects.all().values("id", "title", "description", "price")
        queryset = list(properties_qs)
        cache.set("all_properties", queryset, 3600)
    else:
        print("Fetched property from cache")

    return queryset


def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss metrics and calculate hit ratio.
    """
    # Get default Redis connection
    redis_conn = get_redis_connection("default")

    # Get INFO stats
    info = redis_conn.info(section="stats")
    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)

    total = hits + misses
    hit_ratio = (hits / total) * 100 if total > 0 else 0.0

    metrics = {
        "hits": hits,
        "misses": misses,
        "hit_ratio_percent": round(hit_ratio, 2)
    }

    # Log the metrics
    logger.info(f"Redis Cache Metrics: Hits={hits}, Misses={misses}, Hit Ratio={metrics['hit_ratio_percent']}%")

    return metrics
