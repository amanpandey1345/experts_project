# Generated by Django 4.1.7 on 2023-06-02 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experts_app', '0003_enquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='Course',
            field=models.CharField(max_length=15),
        ),
    ]
