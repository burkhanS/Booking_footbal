import django_filters
from .models import Booking


class BookingFilter(django_filters.FilterSet):
    stadium = django_filters.CharFilter(field_name='stadium', lookup_expr='istartswith')
    status = django_filters.CharFilter(field_name='status', lookup_expr='iexact')

    class Meta:
        model = Booking
        fields = ['stadium', 'status']