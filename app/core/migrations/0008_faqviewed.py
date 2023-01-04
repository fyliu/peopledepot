# Generated by Django 4.0.7 on 2023-01-04 22:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaqViewed',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('faq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.faq')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]