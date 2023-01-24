from django.db import models

# Create your models here.
class Subgalleries(models.Model):
    parent = models.ForeignKey("Gallery", on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    filepath = models.CharField(max_length=248)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=64)
    thumbnail = models.CharField(max_length=248)
    filepath = models.CharField(max_length=248)

    def __str__(self):
        return self.name


class Contact(models.Model):
    title = models.CharField(max_length=80, default="Contact", null=True, blank=True)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=80, default="About", null=True, blank=True)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
