from django.contrib.gis.db import models

# Create your models here.
class Country(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    admin = models.CharField(max_length=1000, blank=True, null=True)
    iso_a3 = models.CharField(max_length=1000, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'

    def __str__(self):
        return self.admin