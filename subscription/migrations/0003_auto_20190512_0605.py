# Generated by Django 2.1.7 on 2019-05-12 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0002_auto_20190512_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='end_date',
            field=models.DateField(null=True),
        ),
    ]
