# Generated by Django 3.2.5 on 2022-05-27 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.shop_user')),
            ],
            options={
                'db_table': 'item',
            },
        ),
        migrations.CreateModel(
            name='Status_delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.item')),
            ],
            options={
                'db_table': 'item-del-status',
            },
        ),
    ]
