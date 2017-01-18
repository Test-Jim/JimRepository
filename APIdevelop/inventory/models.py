from __future__ import unicode_literals

from django.db import models
class testerwork(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=50)
    worktime = models.CharField(max_length=100)
    avgtime = models.CharField(max_length=100)
    txtime = models.CharField(max_length=100)
    csxl = models.CharField(max_length=100)