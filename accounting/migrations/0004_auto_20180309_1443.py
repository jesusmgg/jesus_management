# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-09 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_tax_tax_definition'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('ammount', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='record',
            name='ammount',
        ),
        migrations.RemoveField(
            model_name='record',
            name='description',
        ),
        migrations.RemoveField(
            model_name='tax',
            name='record',
        ),
        migrations.RemoveField(
            model_name='tax',
            name='tax_definition',
        ),
        migrations.AddField(
            model_name='tax',
            name='name',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tax',
            name='rate',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='TaxDefinition',
        ),
        migrations.AddField(
            model_name='recorditem',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Record'),
        ),
        migrations.AddField(
            model_name='recorditem',
            name='tax',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounting.Tax'),
        ),
    ]
