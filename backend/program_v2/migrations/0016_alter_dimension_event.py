# Generated by Django 5.0.6 on 2024-06-13 07:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0040_rename_emailverificationtoken_person_state_core_emailv_person__722147_idx_and_more"),
        ("program_v2", "0015_rename_override_color_dimensionvalue_color_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dimension",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="program_dimensions", to="core.event"
            ),
        ),
    ]
