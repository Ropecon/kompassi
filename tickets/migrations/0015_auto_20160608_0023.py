# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-07 21:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0014_auto_20160305_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketseventmeta',
            name='contact_email',
            field=models.CharField(blank=True, help_text='Ongelmatilanteissa k\xe4ytt\xe4j\xe4\xe4 kehotetaan ottamaan yhteytt\xe4 t\xe4h\xe4n osoitteeseen. Muoto: Tracon 9 -lipunmyynti &lt;liput@tracon.fi&gt;', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('(?P<name>.+) <(?P<email>.+@.+\\..+)'))], verbose_name='Asiakaspalvelun s\xe4hk\xf6postiosoite selitteineen'),
        ),
    ]