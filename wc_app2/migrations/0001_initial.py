# Generated by Django 2.2.7 on 2019-11-15 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=16)),
                ('s_age', models.IntegerField(default=1)),
            ],
        ),
    ]
