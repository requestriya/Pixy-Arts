# Generated by Django 3.0.7 on 2020-11-23 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20201123_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(default='User', max_length=30),
        ),
    ]
