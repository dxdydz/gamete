# Generated by Django 3.0.3 on 2020-04-22 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookwyrm', '0033_auto_20200422_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='importjob',
            name='import_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bookwyrm.Status'),
        ),
    ]
