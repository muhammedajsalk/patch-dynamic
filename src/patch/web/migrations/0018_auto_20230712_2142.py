# Generated by Django 3.1.6 on 2023-07-12 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20230712_2128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'ordering': ['title', '-id'], 'verbose_name': 'Frequently Asked Question', 'verbose_name_plural': 'Frequently Asked Question'},
        ),
        migrations.AlterModelTable(
            name='faq',
            table='web_frequently_asked_questions',
        ),
    ]
