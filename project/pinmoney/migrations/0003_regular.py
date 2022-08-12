# Generated by Django 4.0.6 on 2022-08-11 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pinmoney', '0002_pinmoney_receiver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField()),
                ('unit', models.CharField(max_length=2)),
                ('amount', models.IntegerField()),
                ('type', models.TextField()),
                ('receiver', models.CharField(max_length=100)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
