# Generated by Django 2.1.1 on 2018-09-08 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0008_auto_20180908_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='alertvote',
            name='alert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='alert.Alert'),
        ),
    ]