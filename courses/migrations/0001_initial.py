# Generated by Django 5.0.4 on 2024-04-11 13:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("overview", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="Module",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=200, unique=True)),
            ],
            options={
                "ordering": ["title"],
            },
        ),
    ]