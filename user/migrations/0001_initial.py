# Generated by Django 3.2.7 on 2021-09-24 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('hotelName', models.CharField(default='', max_length=70, verbose_name='Hotel Name')),
                ('typeName', models.CharField(choices=[('Hotel', 'Hotel'), ('Resort', 'Resort'), ('Villa', 'Villa'), ('Farm House', 'Farm House')], default='', max_length=70, verbose_name='Type Name')),
                ('hotel_id', models.CharField(default='', max_length=20, primary_key=True, serialize=False, verbose_name='Account Id')),
                ('email', models.EmailField(max_length=70, verbose_name='Email')),
                ('hotel_url', models.CharField(max_length=50, verbose_name='Hotel Url')),
            ],
        ),
    ]