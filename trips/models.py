from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone

# Todo -
# Getting an error when adding a new overview
# Error about user_id
# Might need to drop the database again
# create new superuser - with kelsey & kp0150 credentials
# Re-login


class User(models.Model):
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Overview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    length = models.IntegerField(default=0)
    season = models.CharField(max_length=200)
    activity_type = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', blank=True)

    # Purpose: output text in python console, rather than the unhelpful <Object object> output
    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Segment(models.Model):
    overview = models.ForeignKey(Overview, on_delete=models.CASCADE)
    province = models.CharField(max_length=200, default='null')
    region = models.CharField(max_length=200, default='null')
    country = models.CharField(max_length=200, default='null')

    # This is arbitrarily set - probably want to change to different data output in the future. Added for same reason as listed above.
    def __str__(self):
        return self.province

# class Transportation(models.Model):
#     transportation_type = models.CharField
#     length = models.IntegerField
#     destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
#

# Create your models here.
