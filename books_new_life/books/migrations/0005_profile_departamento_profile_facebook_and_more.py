# Generated by Django 4.1.1 on 2022-09-30 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0004_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="departamento",
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name="profile",
            name="facebook",
            field=models.URLField(
                blank=True,
                db_index=True,
                default=None,
                max_length=700,
                unique=True,
                verbose_name="Facebook",
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="poblacion",
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name="profile",
            name="profile_pic",
            field=models.ImageField(blank=True, null=True, upload_to="images/profile/"),
        ),
        migrations.AddField(
            model_name="profile",
            name="telefono",
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AddField(
            model_name="profile",
            name="whatsApp",
            field=models.CharField(default=None, max_length=15),
        ),
    ]