from django.db import models
from django.urls import reverse

# Create your models here.


# Django model
class Django(models.Model):
    title = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    body = models.TextField(null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def get_absolute_url(self):
        return reverse("django_detail", kwargs={"pk": self.pk})
