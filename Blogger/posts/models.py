from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    """
    title : char field (max 2048)
    content : text field.
    is_published : boolean field, default is True.
    published_at : datetime field, default is now.
    """

    title=models.CharField(max_length=300)
    content=models.TextField()
    is_published=models.BooleanField(default=True)
    published_at=models.DateTimeField(default=timezone.now)
    poster = models.ImageField(upload_to='posts/images/', default="images/defult.png")


