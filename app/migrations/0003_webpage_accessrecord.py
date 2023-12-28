# Generated by Django 4.2.7 on 2023-12-28 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_webpage_topic_name_delete_accessrecord_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('topic_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topic')),
            ],
        ),
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('author', models.CharField(max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.webpage')),
            ],
        ),
    ]