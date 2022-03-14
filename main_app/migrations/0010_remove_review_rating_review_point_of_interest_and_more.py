# Generated by Django 4.0.3 on 2022-03-14 16:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
        migrations.AddField(
            model_name='review',
            name='point_of_interest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.point_of_interest'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='ratings',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]