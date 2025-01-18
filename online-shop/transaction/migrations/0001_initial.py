# Generated by Django 4.2.4 on 2023-09-16 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.PositiveSmallIntegerField(choices=[(1, 'Charge'), (2, 'Purchase'), (4, 'Transfer')], default=1)),
                ('amount', models.BigIntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('has_score_permission', 'has score permission')],
            },
        ),
        migrations.CreateModel(
            name='UserBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.BigIntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='balance_records', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TransferTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_transaction', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='received_transfers', to='transaction.transaction')),
                ('sender_transaction', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='sent_transfers', to='transaction.transaction')),
            ],
        ),
    ]
