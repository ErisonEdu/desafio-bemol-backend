from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    birth = models.DateField(default='')
    email = models.EmailField(default='')
    cellphone = models.CharField(default='',max_length=11)
    cep = models.CharField(default='', max_length=8)
    street = models.CharField(default='', max_length=100)
    adress_complement = models.CharField(default='', max_length=100)
    district = models.CharField(default='', max_length=100)
    city = models.CharField(default='', max_length=50)
    state = models.CharField(default='', max_length=30)
    DDD = models.CharField(default='', max_length=2)

    def __str__(self):
        return self.name