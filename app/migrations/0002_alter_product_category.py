# Generated by Django 4.1.7 on 2023-03-07 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('TW', 'Top_Wear'), ('BW', 'Bottom_Wear')], max_length=2),
        ),
    ]
