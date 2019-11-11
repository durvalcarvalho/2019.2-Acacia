# Generated by Django 2.2.4 on 2019-11-11 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('status', models.CharField(choices=[('Done', 'Done'), ('Cancelled', 'Cancelled'), ('Open', 'Open'), ('Enough', 'Enough')], max_length=9)),
                ('max_volunteers', models.PositiveSmallIntegerField()),
                ('min_volunteers', models.PositiveSmallIntegerField()),
                ('equipment', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RulesHarvest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=280)),
                ('harvest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='harvest.Harvest')),
            ],
        ),
    ]
