# Generated by Django 3.2.1 on 2023-03-30 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20230327_2320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlepost',
            options={'ordering': ('-created',), 'verbose_name': '标签', 'verbose_name_plural': '标签'},
        ),
        migrations.AlterField(
            model_name='articlecolumn',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
