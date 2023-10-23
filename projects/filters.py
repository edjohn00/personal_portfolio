import django_filters

from .models import *

class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ['title']

    title = django_filters.CharFilter(lookup_expr="icontains", label="Title")

    