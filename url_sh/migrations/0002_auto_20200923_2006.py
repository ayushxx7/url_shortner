# Generated by Django 3.1.1 on 2020-09-23 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_sh', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='short_urls',
            name='long_url',
            field=models.URLField(verbose_name='URL'),
        ),
    ]