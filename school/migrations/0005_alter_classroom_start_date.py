# Generated by Django 3.2.8 on 2022-01-21 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20220121_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
