# Generated by Django 4.1.1 on 2022-09-19 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sahihi_main', '0006_rename_sub_title_portfolioitem_sub_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioitem',
            name='attribution',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
