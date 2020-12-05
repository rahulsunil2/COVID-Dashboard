from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Districts(models.Model):
    districtName = models.CharField(max_length=25)

    def __str__(self):
        return str(self.districtName)


class ContainmentZones(models.Model):
    id = models.AutoField(primary_key=True, db_column='SID')
    district = models.ForeignKey(Districts, on_delete=models.CASCADE)
    area = models.CharField(max_length=40)
    ward = models.CharField(max_length=80)

    def __str__(self):
        return str(self.area)


class EssentialsRequest(models.Model):
    request_id = models.AutoField(primary_key=True, db_column='RID')
    name = models.CharField(max_length=25)
    contact_number = models.IntegerField()
    required_items = models.CharField(max_length=150)

    def __str__(self):
        return str(self.name)
