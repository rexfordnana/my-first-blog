from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.TimeField(default=timezone.now())
    published_date = models.TimeField(null=True,blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
