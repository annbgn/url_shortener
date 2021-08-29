import json
import logging
import uuid
from json.decoder import JSONDecodeError

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

logger = logging.getLogger(__name__)


@require_POST
@csrf_exempt
def get_short_url_view(request):
    """
    returns short url for a long url given in post params
    adds key-value pair in cache for 1h
    """
    try:
        data = json.loads(request.body)
        long_url = data.get("url")
    except (KeyError, JSONDecodeError) as exc:
        logger.exception(exc)
        return HttpResponse(status=400)

    short_url = uuid.uuid4()

    cache.set(short_url, long_url, timeout=60 * 60)  # in seconds
    return HttpResponse(
        json.dumps({"short_url": "localhost:8000/redirect/{}".format(short_url)}),
        status=200,
    )


@require_GET
@csrf_exempt
def redirect_short_url_view(request, short_url):
    """
    redirects short url to long url from cache
    returns 410 Gone status code if key-value has expired
    """
    long_url = cache.get(str(short_url))
    if not long_url:
        return HttpResponse(status=410)
    return redirect(long_url)
