# Generated by Django 5.1.1 on 2024-09-20 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appObjectStorage', '0003_alter_storedfile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storedfile',
            name='file',
            field=models.FileField(upload_to='objectsstorage/BaiduSyncdisk/objstorage'),
        ),
    ]
