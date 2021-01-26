# Generated by Django 3.1.5 on 2021-01-23 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_starts_with', models.PositiveIntegerField()),
                ('hostel_name', models.CharField(max_length=50)),
                ('menu_img', models.ImageField(upload_to='mess')),
            ],
        ),
    ]
