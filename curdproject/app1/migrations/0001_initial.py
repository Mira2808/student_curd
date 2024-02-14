# Generated by Django 5.0.2 on 2024-02-12 06:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faname', models.CharField(max_length=50)),
                ('phoneno', models.BigIntegerField()),
                ('classno', models.IntegerField()),
                ('cteacher', models.CharField(max_length=100)),
                ('progres', models.CharField(choices=[('high', 'high'), ('good', 'good'), ('medium', 'medium'), ('weak', 'weak')], max_length=50)),
                ('user_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Student',
            },
        ),
    ]