# Generated by Django 2.0.6 on 2018-09-15 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_subscription_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='pago'),
        ),
    ]
