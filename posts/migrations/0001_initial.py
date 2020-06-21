# Generated by Django 3.0.5 on 2020-04-07 22:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=20)),
                ('create_date', models.DateField(default=django.utils.timezone.now)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Location')),
            ],
        ),
    ]
