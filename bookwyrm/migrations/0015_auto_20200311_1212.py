# Generated by Django 3.0.3 on 2020-03-11 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookwyrm', '0014_status_remote_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBlocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('relationship_id', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserFollowRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('relationship_id', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserFollows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('relationship_id', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='followers',
        ),
        migrations.DeleteModel(
            name='UserRelationship',
        ),
        migrations.AddField(
            model_name='userfollows',
            name='user_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userfollows_user_object', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userfollows',
            name='user_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userfollows_user_subject', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userfollowrequest',
            name='user_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userfollowrequest_user_object', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userfollowrequest',
            name='user_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userfollowrequest_user_subject', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userblocks',
            name='user_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userblocks_user_object', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userblocks',
            name='user_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userblocks_user_subject', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='blocks',
            field=models.ManyToManyField(related_name='blocked_by', through='bookwyrm.UserBlocks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='follow_requests',
            field=models.ManyToManyField(related_name='follower_requests', through='bookwyrm.UserFollowRequest', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='followers', through='bookwyrm.UserFollows', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='userfollows',
            constraint=models.UniqueConstraint(fields=('user_subject', 'user_object'), name='userfollows_unique'),
        ),
        migrations.AddConstraint(
            model_name='userfollowrequest',
            constraint=models.UniqueConstraint(fields=('user_subject', 'user_object'), name='userfollowrequest_unique'),
        ),
        migrations.AddConstraint(
            model_name='userblocks',
            constraint=models.UniqueConstraint(fields=('user_subject', 'user_object'), name='userblocks_unique'),
        ),
    ]
