# Generated by Django 3.2.18 on 2023-04-26 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0179_merge_20230426_0011"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookauthor",
            name="author_type",
            field=models.CharField(
                choices=[
                    ("author", "Author"),
                    ("editor", "Editor"),
                    ("translator", "Translator"),
                    ("contributor", "Contributor"),
                    ("preface", "Author of Preface"),
                    ("illustrator", "Illustrator"),
                    ("letterer", "Letterer"),
                    ("narrator", "Narrator"),
                    ("other", "Other"),
                ],
                default="author",
                max_length=255,
            ),
        ),
    ]
