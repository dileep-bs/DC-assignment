# Generated by Django 3.2.8 on 2022-01-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_alter_teacher_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'available '), ('NOT_AVAILABLE', 'not available')], default='AVAILABLE', max_length=40),
        ),
    ]
