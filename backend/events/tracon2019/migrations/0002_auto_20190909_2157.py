# Generated by Django 2.1.12 on 2019-09-09 18:57

from django.db import migrations, models

import core.csv_export


class Migration(migrations.Migration):
    dependencies = [
        ("tracon2019", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SignupExtraAfterpartyProxy",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
            },
            bases=("tracon2019.signupextra", core.csv_export.CsvExportMixin),
        ),
        migrations.AlterField(
            model_name="signupextra",
            name="shift_wishes",
            field=models.TextField(
                blank=True,
                help_text="Jos tiedät, ettet pääse paikalle johonkin tiettyyn aikaan tai haluat esimerkiksi osallistua johonkin tiettyyn ohjelmanumeroon, mainitse siitä tässä. HUOM! Muistathan mainita kellonajat (myös ohjelmanumeroista).",
                verbose_name="Työvuorotoiveet",
            ),
        ),
        migrations.AlterField(
            model_name="signupextra",
            name="shirt_size",
            field=models.CharField(
                choices=[
                    ("NO_SHIRT", "Ei paitaa"),
                    ("BOTTLE", "Juomapullo"),
                    ("XS", "XS Unisex"),
                    ("S", "S Unisex"),
                    ("M", "M Unisex"),
                    ("L", "L Unisex"),
                    ("XL", "XL Unisex"),
                    ("XXL", "XXL Unisex"),
                    ("3XL", "3XL Unisex"),
                    ("4XL", "4XL Unisex"),
                    ("5XL", "5XL Unisex"),
                    ("LF_XS", "XS Ladyfit"),
                    ("LF_S", "S Ladyfit"),
                    ("LF_M", "M Ladyfit"),
                    ("LF_L", "L Ladyfit"),
                    ("LF_XL", "XL Ladyfit"),
                ],
                default="NO_SHIRT",
                help_text='Ajoissa ilmoittautuneet vänkärit saavat maksuttoman työvoimapaidan tai juomapullon. Valitse tässä haluatko paidan vai juomapullon, sekä paidan koko. Kokotaulukot: <a href="http://www.bc-collection.eu/uploads/sizes/TU004.jpg" target="_blank">unisex-paita</a>, <a href="http://www.bc-collection.eu/uploads/sizes/TW040.jpg" target="_blank">ladyfit-paita</a>',
                max_length=8,
                verbose_name="Swag-valinta",
            ),
        ),
    ]