from django.db import models
from accounts.models import User

# Create your models here.


class Task(models.Model):

    class PriorityChoices(models.TextChoices):
        low = ('Low', 'Low')
        medium = ('Medium', 'Medium')
        high = ('High', 'High')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PriorityChoices.choices, default=PriorityChoices.medium)
    due_date = models.DateField(null=True, blank=True)
    due_date_time = models.TimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-created']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

