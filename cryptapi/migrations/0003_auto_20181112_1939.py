# Generated by Django 2.1.1 on 2018-11-12 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptapi', '0002_provider_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='nonce',
            field=models.CharField(default='', max_length=32, verbose_name='Nonce'),
        ),
    ]