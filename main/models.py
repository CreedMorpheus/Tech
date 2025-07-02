from django.db import models

class MyModel(models.Model):
    image = models.ImageField(upload_to='images/')

from django.db import models

class SiteContent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    audio = models.FileField(upload_to='audios/', blank=True, null=True)

    def __str__(self):
        return self.title
