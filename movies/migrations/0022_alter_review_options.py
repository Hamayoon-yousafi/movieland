# Generated by Django 4.2.6 on 2023-12-20 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0021_movie_total_negative_votes_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-created',)},
        ),
    ]
