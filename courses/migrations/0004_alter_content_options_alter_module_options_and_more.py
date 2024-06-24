# Generated by Django 4.2.7 on 2024-04-14 05:26

import courses.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0003_content_file_image_text_video"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="content",
            options={"ordering": ["order"]},
        ),
        migrations.AlterModelOptions(
            name="module",
            options={"ordering": ["order"]},
        ),
        migrations.AddField(
            model_name="content",
            name="order",
            field=courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="module",
            name="order",
            field=courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
