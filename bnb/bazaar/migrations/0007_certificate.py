# Generated by Django 3.0.8 on 2020-12-16 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0006_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winner', models.CharField(max_length=25)),
            ],
        ),
    ]
