from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=80,
        null=False
    )

    body = models.TextField(
        null=False
    )

    pub_date = models.DateTimeField(
        auto_now_add=True
    )
