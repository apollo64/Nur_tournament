# Generated by Django 2.2.5 on 2020-11-16 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20201116_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
