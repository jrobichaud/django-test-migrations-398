# Generated by Django 4.2.8 on 2023-12-22 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("A", "0003_nothing"),
        ("B", "0002_nothing"),
    ]

    operations = [
        migrations.CreateModel(
            name="B",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "a_foreign_key",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="A.a"
                    ),
                ),
                ("b_field", models.CharField(max_length=50)),
            ],
        ),
    ]
