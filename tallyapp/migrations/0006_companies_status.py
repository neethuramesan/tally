# Generated by Django 4.0.5 on 2022-08-02 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0005_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
