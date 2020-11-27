# Generated by Django 2.2.5 on 2020-11-16 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_1', models.IntegerField(default=0)),
                ('result_2', models.IntegerField(default=0)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='division', to='teams.Division')),
                ('team_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_1', to='teams.Team')),
                ('team_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_2', to='teams.Team')),
            ],
        ),
        migrations.AddField(
            model_name='division',
            name='name_teams',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='division_name_teams', to='teams.Team'),
        ),
    ]
