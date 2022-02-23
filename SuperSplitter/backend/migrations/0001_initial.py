# Generated by Django 4.0.2 on 2022-02-23 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateTimeField()),
                ('email', models.TextField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('date_time', models.DateTimeField()),
                ('place_name', models.TextField(blank=True, max_length=1000, null=True)),
                ('total_spent', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('participants', models.ManyToManyField(blank=True, to='backend.User')),
                ('spender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_spender', to='backend.user')),
                ('tags', models.ManyToManyField(blank=True, to='backend.Tag')),
            ],
        ),
    ]
