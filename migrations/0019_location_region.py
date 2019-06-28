# Generated by Django 2.2.2 on 2019-06-26 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SalesQuery', '0018_remove_sale_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='region',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='SalesQuery.Region'),
            preserve_default=False,
        ),
    ]