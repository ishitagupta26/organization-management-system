# Generated by Django 5.0.7 on 2024-07-23 09:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("org", "0004_delete_userprofile"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="users",
            field=models.ManyToManyField(
                related_name="organizations", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
