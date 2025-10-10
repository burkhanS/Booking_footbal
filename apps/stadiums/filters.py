import django_filters
from .models import Stadium

class StadiumFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='istartswith')
    min_price = django_filters.NumberFilter(field_name='price_per_hour', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price_per_hour', lookup_expr='lte')
    type = django_filters.CharFilter(field_name='type', lookup_expr='in')

    class Meta:
        model = Stadium
        fields = ['min_price', 'max_price', 'type']