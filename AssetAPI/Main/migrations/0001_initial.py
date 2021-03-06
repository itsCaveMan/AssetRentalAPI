# Generated by Django 4.0.3 on 2022-04-03 18:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on_utc', models.DateTimeField(auto_now_add=True)),
                ('last_modified_utc', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('company_name', models.CharField(blank=True, default='', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on_utc', models.DateTimeField(auto_now_add=True)),
                ('last_modified_utc', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('first_name', models.CharField(blank=True, default='', max_length=255)),
                ('middle_name', models.CharField(blank=True, default='', max_length=255)),
                ('last_name', models.CharField(blank=True, default='', max_length=255)),
                ('email', models.EmailField(blank=True, default='', max_length=255)),
                ('identity', models.CharField(blank=True, default='', max_length=255)),
                ('role', models.CharField(choices=[('DRIVER', 'Driver role'), ('STAFF', 'Staff related role'), ('EXECUTIVE', 'Executive related role'), ('UNDEFINED_ROLE', 'Undefined personnel role')], default='UNDEFINED_ROLE', max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Main.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on_utc', models.DateTimeField(auto_now_add=True)),
                ('last_modified_utc', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('level', models.CharField(choices=[('EDUCATION_LOWER', 'EDUCATION_LOWER'), ('EDUCATION_HIGHER', 'EDUCATION_HIGHER'), ('EDUCATION_TERTIARY', 'EDUCATION_TERTIARY'), ('TRAINING_CERTIFICATION', 'TRAINING_CERTIFICATION'), ('UNDEFINED_LEVEL', 'UNDEFINED_LEVEL')], default='UNDEFINED_LEVEL', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VehicleAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on_utc', models.DateTimeField(auto_now_add=True)),
                ('last_modified_utc', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('uuid', models.CharField(default=uuid.uuid4, max_length=255)),
                ('brand', models.CharField(blank=True, default='', max_length=255)),
                ('model', models.CharField(blank=True, default='', max_length=255)),
                ('odometer', models.BigIntegerField(blank=True, default=0)),
                ('color', models.CharField(blank=True, default='', max_length=12)),
                ('registration_number', models.CharField(blank=True, default='', max_length=35)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Main.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on_utc', models.DateTimeField(auto_now_add=True)),
                ('last_modified_utc', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('uuid', models.CharField(default=uuid.uuid4, max_length=255)),
                ('origin_lat_long', models.CharField(blank=True, default='', max_length=255)),
                ('origin_address', models.CharField(blank=True, default='', max_length=255)),
                ('origin_odometer', models.BigIntegerField(blank=True, default=0)),
                ('destination_lat_long', models.CharField(blank=True, default='', max_length=255)),
                ('destination_address', models.CharField(blank=True, default='', max_length=255)),
                ('destination_odometer', models.BigIntegerField(blank=True, default=0)),
                ('initiated_at_datetime', models.DateTimeField(auto_now_add=True)),
                ('concluded_at_datetime', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Main.customer')),
                ('operated_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Main.personnel')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Main.vehicleasset')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GenericAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on_utc', models.DateTimeField(auto_now_add=True)),
                ('last_modified_utc', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('uuid', models.CharField(default=uuid.uuid4, max_length=255)),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Main.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssetFleetRental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on_utc', models.DateTimeField(auto_now_add=True)),
                ('last_modified_utc', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('date_of_rental', models.DateField(auto_now_add=True)),
                ('assets', models.ManyToManyField(to='Main.genericasset')),
                ('vehicles', models.ManyToManyField(to='Main.vehicleasset')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssetCrossAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on_utc', models.DateTimeField(auto_now_add=True)),
                ('last_modified_utc', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('assets_crossed', models.ManyToManyField(to='Main.genericasset')),
                ('assigned_customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assigned_to_customer', to='Main.customer')),
                ('fleet_rental_where_crossed', models.ManyToManyField(to='Main.assetfleetrental')),
                ('owning_customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='owner_customer', to='Main.customer')),
                ('vehicles_crossed', models.ManyToManyField(to='Main.vehicleasset')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
