from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('open', 'Open'),
    ]
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': False})
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='in_progress')
    deadline = models.DateTimeField(default=now)
    addedby = models.ForeignKey(User, related_name="added_tasks", on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)  # Add description field

    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"

