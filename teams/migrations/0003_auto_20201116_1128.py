# Generated by Django 2.2.5 on 2020-11-16 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20201116_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='division',
            name='name_teams',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='division_name_teams', to='teams.Team'),
        ),
    ]
