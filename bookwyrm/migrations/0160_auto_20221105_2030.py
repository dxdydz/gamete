# Generated by Django 3.2.15 on 2022-11-05 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0159_auto_20220924_0634"),
    ]

    operations = [
        migrations.AddField(
            model_name="importitem",
            name="task_id",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="importjob",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("active", "Active"),
                    ("complete", "Complete"),
                    ("stopped", "Stopped"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
