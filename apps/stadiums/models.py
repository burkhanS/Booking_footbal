from django.db import models

# Create your models here.

class Stadium(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.IntegerField()
    type = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    owner = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name='owned_stadiums')

    def __str__(self):
        return self.name

class StadiumImage(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='stadiums/', blank=True, null=True)

    def __str__(self):
        return self.stadium

# class StadiumAvailability(models.Model):
#     stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name='StadiumAvailability')
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#
#     def __str__(self):
#         return self.stadium.name