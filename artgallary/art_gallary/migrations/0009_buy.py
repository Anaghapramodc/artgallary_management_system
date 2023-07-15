# Generated by Django 4.2.2 on 2023-07-12 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('art_gallary', '0008_compitition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone_no', models.CharField(max_length=15)),
                ('address_1', models.CharField(max_length=200)),
                ('address_2', models.CharField(max_length=200)),
                ('address_3', models.CharField(max_length=200)),
                ('pin', models.CharField(max_length=6)),
                ('nearest_city', models.CharField(max_length=200)),
                ('online_payment', models.BooleanField(default=False)),
                ('cash_on_delivery', models.BooleanField(default=False)),
                ('painting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buy_paintings', to='art_gallary.artist_sell')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
