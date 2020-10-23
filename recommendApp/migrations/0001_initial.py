# Generated by Django 3.1.2 on 2020-10-22 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='NAME')),
                ('local', models.CharField(max_length=100, verbose_name='LOCAL')),
                ('rating', models.IntegerField()),
                ('q1', models.BooleanField(default=False)),
                ('q2', models.BooleanField(default=False)),
                ('q3', models.BooleanField(default=False)),
            ],
        ),
    ]