# Generated by Django 3.2.9 on 2021-11-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bakery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default_image.jpeg', upload_to='uploads/products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
