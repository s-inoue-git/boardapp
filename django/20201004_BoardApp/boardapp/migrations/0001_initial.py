# Generated by Django 3.1.2 on 2020-10-04 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('images', models.ImageField(upload_to='')),
                ('good', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
