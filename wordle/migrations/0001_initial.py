# Generated by Django 4.1.1 on 2022-09-20 03:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="WordleHistory",
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
                ("word", models.CharField(max_length=10)),
                ("length", models.IntegerField(default=5)),
                ("duplicates", models.BooleanField(default=False)),
                ("tries", models.IntegerField(default=6)),
                ("cleared", models.BooleanField(default=False)),
                ("attempted_at", models.DateTimeField(auto_now_add=True)),
                (
                    "player",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wordlehistory",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
