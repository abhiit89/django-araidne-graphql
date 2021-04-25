# Generated by Django 3.2 on 2021-04-25 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=20)),
                ('school_population', models.IntegerField(default=100)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
