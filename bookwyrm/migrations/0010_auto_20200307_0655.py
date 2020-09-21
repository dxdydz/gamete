# Generated by Django 3.0.3 on 2020-03-07 06:55

import datetime
from django.db import migrations, models
import django.db.models.deletion
import bookwyrm.utils.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bookwyrm', '0009_status_published_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bookwyrm.Book')),
                ('isbn', models.CharField(max_length=255, null=True, unique=True)),
                ('oclc_number', models.CharField(max_length=255, null=True, unique=True)),
                ('pages', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('bookwyrm.book',),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bookwyrm.Book')),
                ('lccn', models.CharField(max_length=255, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('bookwyrm.book',),
        ),
        migrations.RemoveField(
            model_name='author',
            name='data',
        ),
        migrations.RemoveField(
            model_name='book',
            name='added_by',
        ),
        migrations.RemoveField(
            model_name='book',
            name='data',
        ),
        migrations.AddField(
            model_name='author',
            name='aliases',
            field=bookwyrm.utils.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, size=None),
        ),
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='born',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='died',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default='Unknown', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='wikipedia_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='first_published_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='last_sync_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='book',
            name='librarything_key',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='book',
            name='local_edits',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='local_key',
            field=models.CharField(default=uuid.uuid4, max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='book',
            name='misc_identifiers',
            field=bookwyrm.utils.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='origin',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='series',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='series_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='sort_title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='subtitle',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='sync',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default='Unknown', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='openlibrary_key',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='openlibrary_key',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='book',
            name='parent_work',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bookwyrm.Work'),
        ),
    ]
