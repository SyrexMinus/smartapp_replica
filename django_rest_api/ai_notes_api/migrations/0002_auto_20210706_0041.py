# Generated by Django 3.2.4 on 2021-07-06 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_notes_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='author',
        ),
        migrations.RemoveField(
            model_name='note',
            name='quote',
        ),
        migrations.AddField(
            model_name='note',
            name='extracted_dates',
            field=models.TextField(default='No citation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='extracted_times',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='input_text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
