# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-09 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('ammount', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Taxes',
            },
        ),
        migrations.CreateModel(
            name='TaxDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rate', models.DecimalField(decimal_places=2, default=10.0, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounting.Record')),
            ],
            bases=('accounting.record',),
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounting.Record')),
            ],
            bases=('accounting.record',),
        ),
        migrations.AddField(
            model_name='tax',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Record'),
        ),
    ]
