# Generated by Django 3.0.3 on 2020-02-21 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookwyrm', '0005_auto_20200221_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='identifier',
            field=models.CharField(max_length=100),
        ),
    ]
