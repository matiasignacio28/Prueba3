# Generated by Django 4.0.4 on 2022-07-10 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_subscribe_subscriber_subscribe_subscribers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subscribe',
        ),
    ]