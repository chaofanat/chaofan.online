# Generated by Django 5.1.1 on 2024-09-20 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appObjectStorage", "0002_storedfile_is_deleted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="storedfile",
            name="file",
            field=models.FileField(upload_to="objectsstorage/BaiduSyncdisk"),
        ),
    ]