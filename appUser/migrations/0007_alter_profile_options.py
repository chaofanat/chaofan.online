# Generated by Django 5.1.1 on 2024-09-20 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("appUser", "0006_alter_profile_options"),
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
    ]