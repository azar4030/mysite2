# Generated by Django 2.2.12 on 2021-09-23 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210923_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryAbout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='public/img/galleries')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
    ]
