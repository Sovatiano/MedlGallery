import django_filters
from .models import *
from django import forms


class PictureFilter(django_filters.FilterSet):
    class Meta:
        model = MedlPicture
        fields = ['name', 'author', 'tags']