# Generated by Django 4.2.8 on 2023-12-22 21:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("A", "0007_fill_new_field"),
    ]

    operations = [
        migrations.AlterField(
            model_name="a",
            name="new_field",
            field=models.CharField(max_length=50),
        ),
    ]