# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-12 21:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20190212_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runningmovie',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movie.Movie'),
        ),
        migrations.AlterField(
            model_name='runningmovie',
            name='theatre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theatres', to='movie.Theatre'),
        ),
        migrations.AlterField(
            model_name='theatre',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='movie.City'),
        ),
    ]