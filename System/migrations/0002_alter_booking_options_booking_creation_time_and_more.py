# Generated by Django 5.1.4 on 2025-01-07 15:28

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['start_time'], 'verbose_name': 'Booking', 'verbose_name_plural': 'Bookings'},
        ),
        migrations.AddField(
            model_name='booking',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 7, 15, 27, 23, 70966, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='System.room'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 7, 15, 28, 18, 356665, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
