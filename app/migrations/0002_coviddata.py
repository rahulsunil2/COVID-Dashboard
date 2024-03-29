# Generated by Django 2.1.15 on 2020-12-08 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CovidData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalConfirmed', models.IntegerField()),
                ('activeCases', models.IntegerField()),
                ('recoveredCases', models.IntegerField()),
                ('totalDeaths', models.IntegerField()),
                ('updateDate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
