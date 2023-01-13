from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment

from datetime import datetime
def get_year_diff(year):
    diff = datetime.now().year - int(year)
    return diff
    
def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'get_year_diff': get_year_diff
    })
    return env


class CustomClass:
    
    def __init__(self, max_length, *args, **kwargs):
        