# Generated by Django 2.2 on 2021-05-29 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validated_show_app', '0002_auto_20210529_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]