# Generated by Django 3.1.6 on 2023-07-12 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20230711_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]