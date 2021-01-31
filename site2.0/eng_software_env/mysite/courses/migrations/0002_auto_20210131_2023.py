# Generated by Django 3.1.5 on 2021-01-31 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('especialidade', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=200)),
                ('canal', models.CharField(max_length=200)),
                ('duracao', models.DurationField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='site',
            name='canal',
        ),
        migrations.RemoveField(
            model_name='site',
            name='duracao',
        ),
    ]