# Generated by Django 2.2.2 on 2019-06-24 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SalesQuery', '0005_budget'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SalesQuery.Budget')),
                ('capability', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SalesQuery.Capability')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SalesQuery.Customer')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SalesQuery.Location')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SalesQuery.Sector')),
            ],
        ),
    ]