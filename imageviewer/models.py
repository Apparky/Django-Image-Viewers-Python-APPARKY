from django.db import models


# Create your models here.
class Post_info(models.Model):
    topic = models.CharField(max_length=300)
    description = models.TextField()
    images = models.FileField(upload_to='midea/images', blank=True)
    img_alt = models.CharField(max_length=100, null=True, blank=True, default='image_alt')

    def __str__(self):
        return self.topic
