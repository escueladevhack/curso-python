from django.db import models


class Post(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    title = models.CharField(
        max_length=80,
        null=False
    )

    body = models.TextField(
        null=False
    )

    pub_date = models.DateTimeField(
        null=False,
        auto_now_add=True,
    )

    def __str__(self):
        return "{}".format(self.title)
