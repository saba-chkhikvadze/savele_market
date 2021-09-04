from django.db.models import fields
import django_filters
from .models import *
from django_filters.conf import DEFAULTS


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['have', 'nakad_has', 'wants', 'nakad_wants']
