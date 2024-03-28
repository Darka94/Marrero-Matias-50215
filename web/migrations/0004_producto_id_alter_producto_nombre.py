# Generated by Django 5.0.3 on 2024-03-28 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_producto_created_at_producto_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
