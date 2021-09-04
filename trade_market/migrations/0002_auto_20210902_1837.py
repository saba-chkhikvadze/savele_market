# Generated by Django 3.2.5 on 2021-09-02 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trade_market', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='nakad',
        ),
        migrations.AddField(
            model_name='post',
            name='nakad_has',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='nakad_wants',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='have',
            field=models.CharField(choices=[('Beshumi', 'Beshumi'), ('Ufliscixe', 'Ufliscixe'), ('Fari', 'Fari'), ('Archeviti', 'Archeviti')], default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='wants',
            field=models.CharField(choices=[('Beshumi', 'Beshumi'), ('Ufliscixe', 'Ufliscixe'), ('Fari', 'Fari'), ('Archeviti', 'Archeviti')], default=None, max_length=50),
        ),
    ]
