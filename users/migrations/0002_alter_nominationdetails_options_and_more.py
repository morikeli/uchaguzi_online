# Generated by Django 4.1.6 on 2023-02-20 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nominationdetails',
            options={'ordering': ['officer_name'], 'verbose_name_plural': 'Officer Nomination Details'},
        ),
        migrations.RemoveField(
            model_name='nominationdetails',
            name='aspirant_school',
        ),
        migrations.RemoveField(
            model_name='nominationdetails',
            name='electoral_post',
        ),
        migrations.RemoveField(
            model_name='nominationdetails',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='nominationdetails',
            name='name',
        ),
        migrations.AddField(
            model_name='nominationdetails',
            name='officer_name',
            field=models.CharField(default='', editable=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='nominationdetails',
            name='aspirant_name',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, to='users.aspirants'),
        ),
    ]
