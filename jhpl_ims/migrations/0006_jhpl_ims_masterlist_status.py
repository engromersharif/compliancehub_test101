# Generated by Django 4.2.3 on 2023-07-24 17:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("jhpl_ims", "0005_remove_jhpl_ims_masterlist_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="jhpl_ims_masterlist",
            name="status",
            field=models.CharField(
                choices=[("A", "Active"), ("O", "Obsolete")],
                default=django.utils.timezone.now,
                max_length=1,
            ),
            preserve_default=False,
        ),
    ]