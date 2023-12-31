# Generated by Django 4.2.5 on 2023-11-08 15:46

from django.db import migrations, models
import whiskeys.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Drink",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=whiskeys.models.drink_upload_path,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Flavor",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=whiskeys.models.flavor_upload_path,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserNumbers",
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
                ("number", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Whiskey",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField()),
                (
                    "whiskey_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=whiskeys.models.whiskey_upload_path,
                    ),
                ),
                ("drink", models.ManyToManyField(blank=True, to="whiskeys.drink")),
                ("flavor", models.ManyToManyField(blank=True, to="whiskeys.flavor")),
            ],
        ),
    ]
