# Generated by Django 2.0.7 on 2018-07-28 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('education_rate', models.IntegerField()),
                ('population_density', models.IntegerField(blank=True, null=True)),
                ('visited', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Divisions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('population', models.IntegerField()),
                ('area', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='districts',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.Divisions'),
        ),
    ]
