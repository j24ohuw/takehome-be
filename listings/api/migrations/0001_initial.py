# Generated by Django 3.2.7 on 2021-10-02 13:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.SlugField()),
                ('state', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ZillowData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_estimate', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000)])),
                ('rent_estimate_last_updated', models.DateField(null=True)),
                ('estimate_amount', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000)])),
                ('estimate_last_updated', models.DateField()),
                ('zillow_id', models.IntegerField()),
                ('link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_unit', models.CharField(default='SqFt', max_length=10)),
                ('bathrooms', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('bedrooms', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('home_size', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('property_size', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('home_type', models.CharField(max_length=50)),
                ('last_sold_date', models.DateField(blank=True, null=True)),
                ('last_sold_price', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000)])),
                ('rent_price', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000)])),
                ('tax_value', models.FloatField()),
                ('tax_year', models.IntegerField()),
                ('year_built', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1800), django.core.validators.MaxValueValidator(2100)])),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000)])),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.address')),
                ('zillow_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.zillowdata')),
            ],
        ),
    ]
