# Generated by Django 4.2 on 2023-05-13 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_alter_review_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image_url',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
