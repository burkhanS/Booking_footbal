from django.db import models


class Review(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='reviews')
    stadium = models.ForeignKey("stadiums.Stadium", on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=0)
    comment = models.TextField(max_length=300, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user

    class Meta:
        unique_together = ('user', 'stadium')
        ordering = ['-created_at']


class Favorite(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='likes')
    stadium = models.ForeignKey("stadiums.Stadium", on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return self.user

    class Meta:
        unique_together = ('user', 'stadium')