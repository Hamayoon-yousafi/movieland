# Generated by Django 4.2.6 on 2023-12-20 09:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cast',
            name='birth_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cast',
            name='birth_place',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cast',
            name='full_bio',
            field=models.TextField(default=django.utils.timezone.now, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cast',
            name='height',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cast',
            name='quote',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='cast',
            name='weight',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='CastImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cast_extra_images')),
                ('cast_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cast.cast')),
            ],
        ),
    ]
