# Generated by Django 4.2.1 on 2023-05-24 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageviewer', '0003_alter_post_info_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_info',
            name='img_alt',
            field=models.CharField(blank=True, default='image_alt', max_length=100, null=True),
        ),
    ]
