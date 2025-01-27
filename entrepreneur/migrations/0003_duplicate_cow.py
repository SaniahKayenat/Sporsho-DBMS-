# Generated by Django 4.2 on 2023-05-24 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrepreneur', '0002_cow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duplicate_cow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cow_name', models.CharField(blank=True, max_length=30)),
                ('month', models.CharField(blank=True, default='', max_length=10)),
                ('year', models.CharField(blank=True, default='', max_length=4)),
                ('dewarming_date', models.DateField()),
                ('torka', models.CharField(blank=True, default='', max_length=15)),
                ('torka_date', models.DateField()),
                ('kurha', models.CharField(blank=True, default='', max_length=15)),
                ('kurha_date', models.DateField(null=True)),
                ('badla', models.CharField(blank=True, default='', max_length=15)),
                ('badla_date', models.DateField()),
                ('name_of_the_disease', models.CharField(blank=True, default='', max_length=20)),
                ('details_on_the_disease', models.CharField(blank=True, default='', max_length=50)),
                ('medications', models.CharField(blank=True, default='', max_length=30)),
                ('monthly_food_expenditure', models.IntegerField(default=0, null=True)),
                ('current_weight', models.IntegerField(default=0, null=True)),
                ('updated_image', models.ImageField(blank=True, default='', null=True, upload_to='')),
            ],
        ),
    ]
