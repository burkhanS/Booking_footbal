from django.db import models

# Create your models here.


class Booking(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name='bookings', null=False, blank=False)
    stadium = models.ForeignKey("stadiums.Stadium", on_delete=models.PROTECT, related_name='bookings')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20,
                              choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
