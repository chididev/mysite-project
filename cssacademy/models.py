from django.db import models
from django.urls import reverse

# Create your models here.


# css model
class Css(models.Model):
    title = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    body = models.TextField(null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def get_absolute_url(self):
        return reverse("css_detail", kwargs={"pk": self.pk})
