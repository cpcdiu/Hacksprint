# Generated by Django 3.0.7 on 2020-11-14 13:27

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', ckeditor.fields.RichTextField()),
                ('education_requirements', models.TextField()),
                ('experience_requirements', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('salary_min', models.IntegerField(blank=True)),
                ('salary_max', models.IntegerField()),
                ('vacancy', models.IntegerField()),
                ('employment_status', models.CharField(choices=[('part-time', 'Part Time'), ('full-time', 'Full Time'), ('internship', 'Internship')], max_length=20)),
                ('office_time', models.CharField(max_length=100)),
                ('deadline', models.DateTimeField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.FileField(upload_to='job/cvs')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.Job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Profile')),
            ],
        ),
    ]
