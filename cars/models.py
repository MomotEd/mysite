from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from .validators import validate_year
from users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import openpyxl
from utils import get_mongo_database
from django.utils.translation import ugettext as _


class Car(models.Model):
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
        ordering = ['name']

    name = models.CharField(max_length=30)
    mpg = models.CharField(max_length=30)
    cylinders = models.CharField(max_length=30)
    displacement = models.CharField(max_length=30)
    horsepower = models.CharField(max_length=30)
    weight = models.CharField(max_length=30)
    acceleration = models.CharField(max_length=30)
    year = models.PositiveIntegerField(validators=[validate_year])
    price = models.CharField(max_length=30)
    origin = models.CharField(max_length=40)

    def __unicode__(self):
        return u'{0} | {1} | {2} | {3} | {4} | {5}'.format(
            self.name, self.cylinders, self.horsepower, self.weight, self.year,
            self.price
        )

    def get_absolute_url(self):
        return reverse('cars:car_detail', kwargs={'car_id': self.id})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]


class Comments(models.Model):
    car = models.ForeignKey(Car)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.comment


class Catalog(models.Model):
    file = models.FileField()
    upload_date = models.DateTimeField()


@receiver(post_save, sender=Catalog)
def save_cars(sender, instance, **kwargs):
    excel_file = instance.file.file
    wb = openpyxl.load_workbook(excel_file)
    ws = wb.active
    for row in ws.rows:
        newcar = Car()
        newcar.name = row[0].value
        newcar.mpg = row[1].value
        newcar.cylinders = row[2].value
        newcar.displacement = row[3].value
        newcar.horsepower = row[4].value
        newcar.weight = row[5].value
        newcar.acceleration = row[6].value
        newcar.year = row[7].value
        newcar.price = row[8].value
        newcar.origin = row[9].value
        newcar.save()


@receiver(post_save, sender=Car)
def save_to_mongodb(sender, instance, **kwargs):
    db = get_mongo_database()
    mongocars = db.cars
    mongocars.remove({"sql_id": instance.id})
    mongocar = {'name': instance.name,
                'mpg': instance.mpg,
                'cylinders': instance.cylinders,
                'displacement': instance.displacement,
                'horsepower': instance.horsepower,
                'weight': instance.weight,
                'acceleration': instance.acceleration,
                'year': instance.year,
                'price': instance.price,
                'origin': instance.origin,
                'sql_id': instance.id}
    mongocars.insert(mongocar)