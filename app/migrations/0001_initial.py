# Generated by Django 4.0.1 on 2022-02-18 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('restId', models.AutoField(db_column='restId', primary_key=True, serialize=False)),
                ('restName', models.TextField(db_column='restName')),
                ('phone', models.IntegerField()),
                ('address', models.TextField()),
                ('ratings', models.DecimalField(decimal_places=1, max_digits=2)),
                ('cuisine', models.TextField()),
                ('region', models.TextField()),
                ('last_modify_date', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'restaurant',
                'managed': True,
            },
        ),
    ]
