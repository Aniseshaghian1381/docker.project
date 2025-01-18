# Generated by Django 4.2.4 on 2023-09-16 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveBigIntegerField(default=0)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='partner.partner')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partners', to='catalogue.product')),
            ],
        ),
    ]
