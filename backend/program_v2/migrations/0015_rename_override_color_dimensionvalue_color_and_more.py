# Generated by Django 5.0.4 on 2024-06-01 13:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("program_v2", "0014_program_cached_earliest_start_time_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="dimensionvalue",
            old_name="override_color",
            new_name="color",
        ),
        migrations.RemoveField(
            model_name="dimension",
            name="color",
        ),
        migrations.RemoveField(
            model_name="dimension",
            name="icon",
        ),
        migrations.RemoveField(
            model_name="dimensionvalue",
            name="override_icon",
        ),
        migrations.AddField(
            model_name="dimension",
            name="is_list_filter",
            field=models.BooleanField(
                default=True, help_text="Suggests to UI that this dimension should be shown as a list filter."
            ),
        ),
        migrations.AddField(
            model_name="dimension",
            name="is_multi_value",
            field=models.BooleanField(
                default=False,
                help_text="Suggests to UI that this dimension is likely to have multiple values selected. NOTE: In the database, all dimensions are multi-value, so this is just a UI hint.",
            ),
        ),
        migrations.AddField(
            model_name="dimension",
            name="is_negative_selection",
            field=models.BooleanField(
                default=False,
                help_text="Suggests to UI that when this dimension is not being filtered on, all values should be selected. Intended for use cases when the user is expected to rather exclude certain values than only include some. One such use case is accessibility and content warnings. NOTE: Does not make sense without `is_multi_value`.",
            ),
        ),
        migrations.AddField(
            model_name="dimension",
            name="is_shown_in_detail",
            field=models.BooleanField(
                default=True, help_text="Suggests to UI that this dimension should be shown in detail view."
            ),
        ),
        migrations.AddField(
            model_name="program",
            name="cached_color",
            field=models.CharField(blank=True, default="", max_length=15),
        ),
        migrations.AddField(
            model_name="program",
            name="cached_location",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name="scheduleitem",
            name="cached_location",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name="program",
            name="cached_earliest_start_time",
            field=models.DateTimeField(
                blank=True,
                help_text="The earliest start time of any schedule item of this program. NOTE: This is not the same as the program's start time. The intended purpose of this field is to exclude programs that have not yet started. Always use `scheduleItems` for the purpose of displaying program times.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="program",
            name="cached_latest_end_time",
            field=models.DateTimeField(
                blank=True,
                help_text="The latest end time of any schedule item of this program. NOTE: This is not the same as the program's start end. The intended purpose of this field is to exclude programs that have already ended. Always use `scheduleItems` for the purpose of displaying program times.",
                null=True,
            ),
        ),
    ]
