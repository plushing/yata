# Generated by Django 3.0.1 on 2020-03-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0017_auto_20200311_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='revive',
            name='reviver_faction',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='revive',
            name='reviver_factionname',
            field=models.CharField(blank=True, default='reviver_factionname', max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='revive',
            name='reviver_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='revive',
            name='reviver_name',
            field=models.CharField(default='reviver_name', max_length=32),
        ),
    ]
