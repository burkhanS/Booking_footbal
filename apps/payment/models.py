import uuid
from django.contrib.auth import get_user_model
from django.db import models
from apps.booking.models import Booking

User = get_user_model()

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
    provider = models.CharField(max_length=50, choices=PROVIDER_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.transaction_id:
            self.transaction_id = f"TXN-{uuid.uuid4().hex[:10].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.booking.user.username}-{self.amount} ({self.status})"


