# Generated by Django 4.0.6 on 2022-08-11 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mission', '0002_alter_mission_date_alter_mission_receiver_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MissionList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]
