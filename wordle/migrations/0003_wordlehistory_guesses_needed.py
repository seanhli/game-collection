# Generated by Django 4.1.1 on 2022-09-20 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wordle", "0002_alter_wordlehistory_duplicates_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="wordlehistory",
            name="guesses_needed",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
