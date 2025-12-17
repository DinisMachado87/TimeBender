from django.db import models
from django.contrib.auth.models import User

class Period(models.Model):
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="periods")

    def __str__(self):
        return self.title
