# Generated by Django 3.1.7 on 2021-03-24 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0004_auto_20210324_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
