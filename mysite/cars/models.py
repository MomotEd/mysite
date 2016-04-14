from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from .validators import validate_year
from users.models import User


# class Category(models.Model):
#     name = models.CharField(max_length=40)
#
#     def __unicode__(self):
#         return self.name


class Car(models.Model):
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
        ordering = ['name']

    name = models.CharField(max_length=30)
    mpg = models.PositiveIntegerField()
    cylinders = models.PositiveIntegerField()
    displacement = models.PositiveIntegerField()
    horsepower = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    acceleration = models.FloatField()
    year = models.PositiveIntegerField(validators=[validate_year])
    price = models.CharField(max_length=30)
    origin = models.CharField(max_length=40, help_text='Release country')

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