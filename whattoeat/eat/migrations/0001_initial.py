# Generated by Django 2.2.7 on 2019-11-22 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restuarant_text', models.CharField(max_length=200)),
                ('restuarant_evaluate', models.IntegerField()),
            ],
        ),
    ]
