# Generated by Django 3.1.7 on 2021-03-24 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySite', '0003_auto_20210324_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='digital',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
