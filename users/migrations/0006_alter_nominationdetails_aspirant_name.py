# Generated by Django 4.1.6 on 2023-02-20 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_nominationdetails_has_nominated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nominationdetails',
            name='aspirant_name',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='users.aspirants'),
        ),
    ]
