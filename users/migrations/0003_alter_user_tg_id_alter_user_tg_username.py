# Generated by Django 4.2.7 on 2023-11-28 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_username_user_tg_id_user_tg_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tg_id',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Telegram_id'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tg_username',
            field=models.CharField(default='some_username', max_length=60, unique=True, verbose_name='Ник в тг'),
        ),
    ]
