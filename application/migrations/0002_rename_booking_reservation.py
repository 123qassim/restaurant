# Generated by Django 5.1.3 on 2024-11-19 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booking',
            new_name='Reservation',
        ),
    ]