# Generated by Django 4.1.2 on 2022-10-30 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0005_yearlybill_tenant_house_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='status',
        ),
        migrations.AddField(
            model_name='house',
            name='color',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='house',
            name='is_occupied',
            field=models.BooleanField(default=False),
        ),
    ]
