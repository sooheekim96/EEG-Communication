# Generated by Django 3.0.4 on 2020-03-09 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eeg_parser', '0014_auto_20200308_1308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eeg',
            old_name='title',
            new_name='address',
        ),
        migrations.AddField(
            model_name='eeg',
            name='name',
            field=models.CharField(default='test', max_length=15),
        ),
        migrations.AlterField(
            model_name='callee',
            name='name',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]