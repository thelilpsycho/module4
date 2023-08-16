# Generated by Django 4.2.3 on 2023-08-15 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_advertisements', '0002_alter_advertisement_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default=1, upload_to='advertisements/', verbose_name='изображение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
