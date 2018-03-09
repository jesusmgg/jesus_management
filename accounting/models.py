from decimal import Decimal
from django.db import models
from django.utils import timezone


####################################################################
# RECORDS
####################################################################


class Record(models.Model):
    date = models.DateField(default=timezone.now)
    description = models.CharField(max_length=200)
    ammount = models.DecimalField(default=0.0, decimal_places=2, max_digits=15)


class Income(Record):
    pass


class Expense(Record):
    pass
####################################################################


####################################################################
# TAXES
####################################################################
class TaxDefinition(models.Model):
    name = models.CharField(max_length=30)
    rate = models.DecimalField(default=10.0, decimal_places=2, max_digits=15)

    class Meta:
        verbose_name_plural = 'Tax Definitions'

    def __str__(self):
        return self.name


class Tax(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    tax_definition = models.ForeignKey(TaxDefinition, on_delete=models.PROTECT)

    def ammount(self):
        return self.record.ammount * (self.tax_definition.rate / Decimal(100.0))

    class Meta:
        verbose_name_plural = 'Taxes'
####################################################################
