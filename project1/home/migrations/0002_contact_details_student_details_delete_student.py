# Generated by Django 4.2.7 on 2023-11-15 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='student_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Place', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]
