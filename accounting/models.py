from decimal import Decimal
from django.db import models
from django.utils import timezone


####################################################################
# TAXES
####################################################################
class Tax(models.Model):
    name = models.CharField(max_length=30)
    rate = models.DecimalField(default=10.0, decimal_places=2, max_digits=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Taxes'
####################################################################


####################################################################
# RECORDS
####################################################################
class Record(models.Model):
    date = models.DateField(default=timezone.now)


class RecordItem(models.Model):
    description = models.CharField(max_length=200)
    ammount = models.DecimalField(default=0.0, decimal_places=2, max_digits=15)
    tax = models.ForeignKey(Tax, on_delete=models.PROTECT)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)


class Income(Record):
    pass


class Expense(Record):
    pass
####################################################################
