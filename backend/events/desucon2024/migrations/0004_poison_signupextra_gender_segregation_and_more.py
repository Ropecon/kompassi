# Generated by Django 5.0.4 on 2024-05-22 19:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("desucon2024", "0003_signupextra_accommodation"),
    ]

    operations = [
        migrations.CreateModel(
            name="Poison",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=63)),
            ],
        ),
        migrations.AddField(
            model_name="signupextra",
            name="gender_segregation",
            field=models.CharField(
                choices=[
                    ("m", "Miesten vuoro"),
                    ("f", "Naisten vuoro"),
                    ("x", "Sekasauna"),
                    ("z", "Ei väliä / en sauno"),
                ],
                default="z",
                help_text="Millä saunavuorolla haluat saunoa? Tämä ei sido sinua mihinkään; käytämme tietoa saunavuorojen aikatauluttamiseen.",
                max_length=1,
                verbose_name="Saunavuoro",
            ),
        ),
        migrations.AddField(
            model_name="signupextra",
            name="pick_your_poison",
            field=models.ManyToManyField(
                blank=True, to="desucon2024.poison", verbose_name="Mitä haluaisit juoda kaatajaisissa?"
            ),
        ),
    ]