# Generated by Django 4.1.4 on 2023-02-03 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aspirants',
            fields=[
                ('id', models.CharField(editable=False, max_length=15, primary_key=True, serialize=False, unique=True)),
                ('alias', models.CharField(blank=True, max_length=25)),
                ('bio', models.TextField()),
                ('post', models.CharField(max_length=32)),
                ('slogan', models.CharField(blank=True, max_length=50)),
                ('pic', models.ImageField(upload_to='Aspirant-Dps/')),
                ('form', models.FileField(upload_to='Nomination-Forms/')),
                ('nominate', models.BooleanField(default=False)),
                ('votes', models.PositiveIntegerField(default=0, editable=False)),
                ('applied', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='accounts.voters')),
            ],
            options={
                'verbose_name_plural': 'Aspirants',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Polled',
            fields=[
                ('id', models.CharField(editable=False, max_length=18, primary_key=True, serialize=False, unique=True)),
                ('user_id', models.CharField(editable=False, max_length=20)),
                ('academic', models.BooleanField(default=False, editable=False)),
                ('general_rep', models.BooleanField(default=False, editable=False)),
                ('ladies_rep', models.BooleanField(default=False, editable=False)),
                ('treasurer', models.BooleanField(default=False, editable=False)),
                ('governor', models.BooleanField(default=False, editable=False)),
                ('president', models.BooleanField(default=False, editable=False)),
                ('polled', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Polled',
            },
        ),
        migrations.CreateModel(
            name='Voted',
            fields=[
                ('id', models.CharField(editable=False, max_length=18, primary_key=True, serialize=False, unique=True)),
                ('user_id', models.CharField(editable=False, max_length=20)),
                ('academic', models.BooleanField(default=False, editable=False)),
                ('general_rep', models.BooleanField(default=False, editable=False)),
                ('ladies_rep', models.BooleanField(default=False, editable=False)),
                ('treasurer', models.BooleanField(default=False, editable=False)),
                ('governor', models.BooleanField(default=False, editable=False)),
                ('president', models.BooleanField(default=False, editable=False)),
                ('voted', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Voted',
            },
        ),
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.CharField(editable=False, max_length=15, primary_key=True, serialize=False)),
                ('post', models.CharField(editable=False, max_length=32)),
                ('total_polls', models.PositiveIntegerField(default=0, editable=False)),
                ('percentage', models.DecimalField(decimal_places=1, default=0, editable=False, max_digits=4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='users.aspirants')),
            ],
            options={
                'verbose_name_plural': 'Polls',
                'ordering': ['-total_polls'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.CharField(editable=False, max_length=15, primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('written', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('blogger', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='users.aspirants')),
            ],
            options={
                'verbose_name_plural': 'Blogs',
                'ordering': ['written'],
            },
        ),
    ]
