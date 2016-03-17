import datetime
from django.core.exceptions import ValidationError

OLDEST_CAR_YEAR = 1950


def validate_year(value):
    if not OLDEST_CAR_YEAR <= value <= datetime.datetime.now().year:
        raise ValidationError("Car can not be older 1950 year of release and "
                              "can not be released in future")
    return value
