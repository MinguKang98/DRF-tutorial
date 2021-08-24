# Generated by Django 3.2.6 on 2021-08-15 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120)),
                ('photo', models.ImageField(upload_to='')),
                ('kind', models.CharField(choices=[('actor', 'Actor'), ('director', 'Director')], max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
