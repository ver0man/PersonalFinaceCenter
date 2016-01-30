# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 20:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_person', models.CharField(max_length=30)),
                ('expense_time', models.DateTimeField(auto_now_add=True)),
                ('expense_amount', models.FloatField(default=0)),
                ('expense_text', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'ordering': ['-expense_time', 'expense_person'],
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_person', models.CharField(max_length=30)),
                ('income_time', models.DateTimeField(auto_now_add=True)),
                ('income_amount', models.FloatField(default=0)),
                ('income_text', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'ordering': ['-income_time', 'income_person'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_firstname', models.CharField(max_length=20)),
                ('user_lastname', models.CharField(max_length=20)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_password', models.CharField(max_length=20)),
                ('user_tel', models.CharField(max_length=15)),
                ('user_add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_name', models.CharField(max_length=30, unique=True)),
                ('wallet_income', models.FloatField(default=0)),
                ('wallet_expense', models.FloatField(default=0)),
                ('wallet_total', models.FloatField(default=0)),
                ('wallet_note', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'ordering': ['wallet_name'],
            },
        ),
        migrations.AddField(
            model_name='income',
            name='income_wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashier.Wallet'),
        ),
        migrations.AddField(
            model_name='expense',
            name='expense_wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashier.Wallet'),
        ),
    ]
