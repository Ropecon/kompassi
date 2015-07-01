# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_ticketseventmeta_receipt_footer'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccommodationInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100, verbose_name=b'Etunimi')),
                ('last_name', models.CharField(max_length=100, verbose_name=b'Sukunimi')),
                ('phone_number', models.CharField(max_length=30, null=True, verbose_name=b'Puhelinnumero', blank=True)),
                ('order', models.ForeignKey(related_name='accommodation_information_set', to='tickets.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='requires_accommodation_information',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
