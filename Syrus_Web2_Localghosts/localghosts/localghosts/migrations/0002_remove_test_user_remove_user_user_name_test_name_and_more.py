# Generated by Django 4.1.5 on 2023-03-11 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localghosts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
        migrations.AddField(
            model_name='test',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='test',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='test',
            name='text',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='truck',
            name='destination',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='truck',
            name='driver_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='truck',
            name='origin',
            field=models.CharField(default='', max_length=50),
        ),
    ]
