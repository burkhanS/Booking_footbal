from django.db import models

# Create your models here.
from apps.booking.models import Booking


class Payment(models.Model):
    PROVIDER_CHOICES = (
        ('Payme', 'payme'),
        ('Click', 'click'),
    )

    STATUS_CHOICES = (
        ('pending', 'В ожидании'),
        ('success', 'Успешно'),
        ('failed', 'Ошибка'),
    )
    booking = models.OneToOneField("booking.Booking", on_delete=models.PROTECT, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.CharField(max_length=20, choices=PROVIDER_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.amount


