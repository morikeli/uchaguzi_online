# Generated by Django 4.1.6 on 2023-02-08 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NominationDetails',
            fields=[
                ('id', models.CharField(editable=False, max_length=15, primary_key=True, serialize=False, unique=True)),
                ('gender', models.CharField(max_length=7)),
                ('officer_school', models.CharField(max_length=70)),
                ('role', models.CharField(max_length=25)),
                ('aspirant_name', models.CharField(max_length=100)),
                ('electoral_post', models.CharField(max_length=32)),
                ('candidate_school', models.CharField(max_length=70)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='accounts.officials')),
            ],
            options={
                'verbose_name_plural': 'Officer Nomination Details',
                'ordering': ['name'],
            },
        ),
    ]