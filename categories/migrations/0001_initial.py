# Generated by Django 4.2 on 2023-04-15 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.CharField(max_length=256)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category', to='products.product')),
            ],
        ),
    ]
