# Generated by Django 5.0.7 on 2024-07-24 07:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("org", "0007_team"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="users",
            field=models.ManyToManyField(
                related_name="teams", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
