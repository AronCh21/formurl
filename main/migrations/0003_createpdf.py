# Generated by Django 4.0.6 on 2023-03-13 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_sender'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatePdf',
            fields=[
                ('byOrder', models.CharField(max_length=500)),
                ('tel', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=500)),
                ('nationality', models.CharField(max_length=500)),
                ('sender', models.CharField(max_length=500)),
                ('idNo', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('senderTel', models.CharField(max_length=500)),
                ('porpuse', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=1000)),
                ('time', models.TimeField(blank=True, default='13:52:53')),
                ('valueDate', models.DateField(blank=True, default='03/13/23')),
            ],
        ),
    ]
