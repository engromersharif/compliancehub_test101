# Generated by Django 4.2.3 on 2023-07-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jhpl_ims", "0008_alter_jhpl_ims_masterlist_approved_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jhpl_ims_masterlist",
            name="approved_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="jhpl_ims_masterlist",
            name="control_copy_num",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="jhpl_ims_masterlist",
            name="issue_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="jhpl_ims_masterlist",
            name="reviewed_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="jhpl_ims_masterlist",
            name="status",
            field=models.CharField(
                choices=[
                    ("Active", "Active"),
                    ("Obsolete", "Obsolete"),
                    ("InProcess", "InProcess"),
                ],
                max_length=9,
            ),
        ),
    ]
