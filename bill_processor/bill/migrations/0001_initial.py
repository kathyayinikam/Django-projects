# Generated by Django 4.1.3 on 2024-07-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='bills/')),
                ('rr_number', models.CharField(blank=True, max_length=100)),
                ('account_id', models.CharField(blank=True, max_length=100)),
                ('consumption', models.CharField(blank=True, max_length=100)),
                ('tax', models.CharField(blank=True, max_length=100)),
                ('net_amount_due', models.CharField(blank=True, max_length=100)),
                ('processed', models.BooleanField(default=False)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
