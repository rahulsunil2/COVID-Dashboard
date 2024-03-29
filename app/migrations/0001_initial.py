# Generated by Django 2.1.15 on 2020-11-10 23:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContainmentZones',
            fields=[
                ('id', models.AutoField(db_column='SID', primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=40)),
                ('ward', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('districtName', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='EssentialsRequest',
            fields=[
                ('request_id', models.AutoField(db_column='RID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('contact_number', models.IntegerField()),
                ('required_items', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='containmentzones',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Districts'),
        ),
    ]
