# Generated by Django 3.2.1 on 2023-04-22 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='avatar/%Y%m%d/', verbose_name='头像'),
        ),
    ]