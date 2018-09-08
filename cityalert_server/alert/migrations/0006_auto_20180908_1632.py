# Generated by Django 2.1.1 on 2018-09-08 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0005_auto_20180908_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertTypeRouting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_type', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alert.AlertType')),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='alertresponse',
            name='priority',
            field=models.IntegerField(choices=[(1, 'Bassa'), (2, 'Media'), (3, 'Alta')], default=1),
        ),
        migrations.AddField(
            model_name='alerttyperouting',
            name='office',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alert.Office'),
        ),
        migrations.AddField(
            model_name='alert',
            name='assigned_office',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alert.Office'),
        ),
    ]
