# Generated by Django 4.2.7 on 2023-12-19 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_products_got_it_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='got_it_from',
            field=models.CharField(blank=True, choices=[('محمد محمد حمدون', 'محمد محمد حمدون')], max_length=255, null=True, verbose_name='تم شرائه من'),
        ),
    ]
