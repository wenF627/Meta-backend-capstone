# Generated by Django 4.2.11 on 2024-03-23 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="booking",
            options={
                "verbose_name": "Booking",
                "verbose_name_plural": "Booking Records",
            },
        ),
        migrations.AlterModelOptions(
            name="menu",
            options={"verbose_name": "Menu", "verbose_name_plural": "Menu Items"},
        ),
    ]
