from django.db import models


# Create your models here.


class MedlMember(models.Model):
    nickname = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nickname


class MedlTag(models.Model):
    tagname = models.CharField(max_length=300, null=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    author = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.tagname


class MedlPicture(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    url = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    tags = models.ManyToManyField(MedlTag, blank=True)

    def __str__(self):
        return self.name
