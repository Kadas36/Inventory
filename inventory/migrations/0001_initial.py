# Generated by Django 3.1.6 on 2021-02-02 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('product_name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=0)),
                ('received_quantity', models.IntegerField(default=0)),
                ('receipient', models.CharField(max_length=50)),
                ('issued_quantity', models.IntegerField(default=0)),
                ('issue_by', models.CharField(max_length=50)),
                ('issue_to', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('created_by', models.CharField(max_length=50)),
                ('alert_amount', models.IntegerField(default=0)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
