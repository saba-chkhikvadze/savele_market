# Generated by Django 3.2.5 on 2021-09-03 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trade_market', '0003_auto_20210902_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offered_loc', models.CharField(choices=[('ბეშუმი', 'ბეშუმი'), ('უფლისციხე', 'უფლისციხე'), ('ფარი', 'ფარი'), ('არჩევითი', 'არჩევითი')], max_length=50)),
                ('offered_nakad', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3')])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='trade_market.post')),
            ],
        ),
    ]
