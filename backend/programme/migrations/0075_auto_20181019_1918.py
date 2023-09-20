# Generated by Django 1.10.8 on 2018-10-19 16:18
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("programme", "0074_auto_20180620_1623"),
    ]

    operations = [
        migrations.AlterField(
            model_name="programme",
            name="computer",
            field=models.CharField(
                choices=[
                    ("con", "Laptop provided by the event"),
                    ("pc", "Own laptop – PC"),
                    ("mac", "Own laptop – Mac"),
                    ("none", "No computer required"),
                ],
                default="con",
                help_text="What kind of a computer do you wish to use? The use of your own computer is only possible if agreed in advance.",
                max_length=4,
                verbose_name="Computer use",
            ),
        ),
    ]