# Generated by Django 4.2.6 on 2023-11-27 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]