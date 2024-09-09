# Generated by Django 5.1.1 on 2024-09-05 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appUser", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile",
            options={
                "default_related_name": "profile",
                "get_latest_by": "created_at",
                "ordering": ["-created_at"],
                "verbose_name": "Profile",
                "verbose_name_plural": "Profiles",
            },
        ),
        migrations.AlterField(
            model_name="profile",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]