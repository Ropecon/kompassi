# Generated by Django 1.9.1 on 2016-02-02 20:36


import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("programme", "0023_auto_20160202_2231"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.CharField(
                help_text='Tekninen nimi eli "slug" n\xe4kyy URL-osoitteissa. Sallittuja merkkej\xe4 ovat pienet kirjaimet, numerot ja v\xe4liviiva. Teknist\xe4 nime\xe4 ei voi muuttaa luomisen j\xe4lkeen.',
                max_length=255,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Tekninen nimi saa sis\xe4lt\xe4\xe4 vain pieni\xe4 kirjaimia, numeroita sek\xe4 v\xe4liviivoja.",
                        regex="[a-z0-9-]+",
                    )
                ],
                verbose_name="Tekninen nimi",
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="slug",
            field=models.CharField(
                blank=True,
                help_text='Tekninen nimi eli "slug" n\xe4kyy URL-osoitteissa. Sallittuja merkkej\xe4 ovat pienet kirjaimet, numerot ja v\xe4liviiva. Teknist\xe4 nime\xe4 ei voi muuttaa luomisen j\xe4lkeen.',
                max_length=255,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Tekninen nimi saa sis\xe4lt\xe4\xe4 vain pieni\xe4 kirjaimia, numeroita sek\xe4 v\xe4liviivoja.",
                        regex="[a-z0-9-]+",
                    )
                ],
                verbose_name="Tekninen nimi",
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="slug",
            field=models.CharField(
                help_text='Tekninen nimi eli "slug" n\xe4kyy URL-osoitteissa. Sallittuja merkkej\xe4 ovat pienet kirjaimet, numerot ja v\xe4liviiva. Teknist\xe4 nime\xe4 ei voi muuttaa luomisen j\xe4lkeen.',
                max_length=255,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Tekninen nimi saa sis\xe4lt\xe4\xe4 vain pieni\xe4 kirjaimia, numeroita sek\xe4 v\xe4liviivoja.",
                        regex="[a-z0-9-]+",
                    )
                ],
                verbose_name="Tekninen nimi",
            ),
        ),
    ]