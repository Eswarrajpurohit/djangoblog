# Generated by Django 3.2.4 on 2021-07-17 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20200517_0457'),
    ]

    operations = [
        migrations.CreateModel(
            name='testModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testField', models.CharField(max_length=700000)),
            ],
        ),
    ]
