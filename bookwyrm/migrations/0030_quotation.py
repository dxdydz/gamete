# Generated by Django 3.0.3 on 2020-04-07 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookwyrm', '0029_auto_20200403_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('status_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bookwyrm.Status')),
                ('quote', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookwyrm.Edition')),
            ],
            options={
                'abstract': False,
            },
            bases=('bookwyrm.status',),
        ),
    ]
