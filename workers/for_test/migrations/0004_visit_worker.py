# Generated by Django 4.2.6 on 2023-10-12 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('for_test', '0003_store_latitude_store_longtitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='worker',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='for_test.worker'),
            preserve_default=False,
        ),
    ]