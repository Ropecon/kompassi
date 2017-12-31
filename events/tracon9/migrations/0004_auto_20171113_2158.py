# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-13 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracon9', '0003_signupextra_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupextra',
            name='shift_type',
            field=models.CharField(choices=[('yksipitka', 'Yksi pitkä vuoro'), ('montalyhytta', 'Monta lyhyempää vuoroa'), ('kaikkikay', 'Kumpi tahansa käy')], help_text='Haluatko tehdä yhden pitkän työvuoron vaiko monta lyhyempää vuoroa?', max_length=15, verbose_name='Toivottu työvuoron pituus'),
        ),
        migrations.AlterField(
            model_name='signupextra',
            name='total_work',
            field=models.CharField(choices=[('8h', 'Minimi - 8 tuntia (1 lämmin ateria)'), ('12h', '12 tuntia (2 lämmintä ateriaa)'), ('yli12h', 'Työn Sankari! Yli 12 tuntia! (2 lämmintä ateriaa)')], help_text='Kuinka paljon haluat tehdä töitä yhteensä tapahtuman aikana? Useimmissa tehtävistä minimi on kahdeksan tuntia, mutta joissain tehtävissä se voi olla myös vähemmän (esim. majoitusvalvonta 6 h).', max_length=15, verbose_name='Toivottu kokonaistyömäärä'),
        ),
    ]