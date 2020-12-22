from django.db import models
from django.utils import timezone

# Users and posts are going to have relationship (one to many)
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    # you can use auto_now=True so it will show the time of the post's last updated
    # you can also use auto_now_add=True which will show only the time when the
    # post was created. but then you can't ever update the date.
    # I would like to be able to change the date whenever i want to. so instead,
    # I use default = timezone.now (notice there is no parenthesis)
    date_posted = models.DateTimeField(default=timezone.now)

    # setting up one-to-many relationship between posts and users
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # For showing the title when querying the Post with Post.objects.all()
    def __str__(self):
        return self.title
