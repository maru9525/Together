# Generated by Django 3.2.7 on 2021-10-02 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PointTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(blank=True, max_length=120, null=True)),
                ('order_id', models.CharField(max_length=120, unique=True)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('success', models.BooleanField(default=False)),
                ('transaction_status', models.CharField(blank=True, max_length=220, null=True)),
                ('type', models.CharField(max_length=120)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]