# Generated by Django 3.2.3 on 2021-06-13 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_booking_mobile_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
