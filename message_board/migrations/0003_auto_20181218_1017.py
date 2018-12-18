# Generated by Django 2.0 on 2018-12-18 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_board', '0002_message_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(verbose_name='留言'),
        ),
        migrations.AlterField(
            model_name='message',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='是否公开'),
        ),
        migrations.AlterField(
            model_name='message',
            name='nickname',
            field=models.CharField(max_length=20, verbose_name='昵称'),
        ),
    ]
