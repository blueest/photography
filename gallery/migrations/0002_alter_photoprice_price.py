# Generated by Django 5.1.4 on 2024-12-25 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoprice',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]