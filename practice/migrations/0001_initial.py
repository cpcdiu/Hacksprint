# Generated by Django 3.0.7 on 2020-11-14 13:27

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('desc', models.TextField()),
                ('avatar', models.ImageField(default='default.jpg', upload_to='practice/tracks')),
            ],
        ),
        migrations.CreateModel(
            name='Subdomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice.Track')),
            ],
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('body', ckeditor.fields.RichTextField()),
                ('difficulty', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('subdomain', models.ManyToManyField(to='practice.Subdomain')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice.Track')),
            ],
        ),
    ]
