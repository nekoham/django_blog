# Generated by Django 5.0.4 on 2024-04-29 17:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0004_alter_blog_tag_alter_blog_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="updated_on",
            field=models.DateTimeField(
                auto_now=True, help_text="Date of update", null=True
            ),
        ),
    ]