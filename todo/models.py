from django.db import models

# Create your models here.

class Todo(models.Model):

    title = models.CharField('Title', max_length=50)
    description = models.CharField('Description', max_length=100)
    priority = models.CharField('Priority', max_length=20)
    is_completed = models.BooleanField('Is_completed', default=False)
    completed_at = models.DateTimeField('completed_at', null=True)

    def __str__(self):
        return self.title