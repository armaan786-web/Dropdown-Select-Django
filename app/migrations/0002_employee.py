# Generated by Django 4.0.1 on 2022-02-18 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emplid', models.AutoField(db_column='emplid', primary_key=True, serialize=False)),
                ('name', models.IntegerField()),
                ('address', models.TextField()),
                ('region', models.TextField()),
            ],
            options={
                'db_table': 'Employee',
                'managed': True,
            },
        ),
    ]
