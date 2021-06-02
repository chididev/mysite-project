from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='images/', null=True)
    body = models.TextField(null=True)


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
