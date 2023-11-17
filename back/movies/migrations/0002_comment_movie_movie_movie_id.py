# Generated by Django 4.2.4 on 2023-11-17 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_id',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]