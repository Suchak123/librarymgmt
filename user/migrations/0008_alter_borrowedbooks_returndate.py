# Generated by Django 4.2.6 on 2024-02-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_borrowedbooks_bookid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowedbooks',
            name='ReturnDate',
            field=models.DateField(null=True),
        ),
    ]
