from django.db import models

# Create your models here.
class ItemModel(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [
        ('OWNER', 'Собственность самой организации'),
        ('OTHER', 'Сторонний офис'),
    ]
    equipment_type = models.CharField(max_length=256)
    manufacturer = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    price = models.CharField(max_length=256)
    owner = models.CharField(max_length=256, default='')
    belonging = models.CharField(max_length=256)
    number = models.CharField(max_length=256)
    date_in = models.DateField()
    date_out = models.DateField()