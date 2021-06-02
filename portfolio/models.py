from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    description = models.TextField(null=True)
    tech_title = models.CharField(max_length=200, default='Tech stack used', null=True)
    teck_stack = models.TextField(null=True, default='Python, Html5, CSS3, Bootstrap5')

    def __str__(self):
        return self.title
