# Generated by Django 2.0.5 on 2019-07-13 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_json', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=253)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=521)),
                ('state', models.CharField(max_length=250)),
                ('phone', models.BigIntegerField()),
                ('zip_code', models.IntegerField()),
            ],
        ),
    ]