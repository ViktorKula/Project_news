from django_filters import FilterSet
import django_filters
from django import forms
from .models import Post


class PostFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться
    # (т. е. подбираться) информация о постах
    date = django_filters.DateFilter(field_name='post_date', widget=forms.DateInput(attrs={'type': 'date'}),
                      label='поиск по дате начиная с', lookup_expr='date__gte')

    class Meta:
        model = Post
        fields = {
            'post_title': ['icontains'],

            'post_text': ['icontains']
        }