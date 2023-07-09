# Generated by Django 4.2.3 on 2023-07-09 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_item', models.CharField(max_length=34)),
                ('time_of_refund_request', models.DateTimeField()),
                ('reason_for_refund', models.CharField(max_length=50)),
                ('refund_request_status', models.BooleanField()),
                ('actual_refund_status', models.BooleanField()),
            ],
        ),
    ]