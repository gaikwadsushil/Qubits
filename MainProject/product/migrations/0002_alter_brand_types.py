# Generated by Django 5.1.2 on 2024-10-21 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='types',
            field=models.CharField(choices=[('CPB', 'corporate branding'), ('PSB', 'personal branding'), ('PB', 'product branding'), ('RB', 'Retail branding'), ('GPB', 'Geographic branding'), ('SB', 'Service branding')], max_length=20),
        ),
    ]