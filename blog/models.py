from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    body = models.TextField(null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
