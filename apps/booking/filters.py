import django_filters
from .models import Booking


class BookingFilter(django_filters.FilterSet):
    stadium = django_filters.CharFilter(field_name='stadium', lookup_expr='istartswith')
    date = django_filters.DateFilter(field_name='date', lookup_expr='exact')
    status = django_filters.CharFilter(field_name='status', lookup_expr='iexact')
    min_price = django_filters.NumberFilter(field_name='price_per_hour', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price_per_hour', lookup_expr='lte')

    class Meta:
        model = Booking
        fields = ['stadium', 'date', 'status', 'min_price', 'max_price']