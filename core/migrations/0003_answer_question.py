# Generated by Django 3.2.8 on 2021-10-28 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.question'),
            preserve_default=False,
        ),
    ]
