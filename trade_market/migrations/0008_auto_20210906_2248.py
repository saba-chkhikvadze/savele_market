# Generated by Django 3.2.5 on 2021-09-06 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_market', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]