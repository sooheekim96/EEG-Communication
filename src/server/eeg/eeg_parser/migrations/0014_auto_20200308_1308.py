# Generated by Django 3.0.4 on 2020-03-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eeg_parser', '0013_auto_20200306_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callee',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]