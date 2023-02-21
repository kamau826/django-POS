# Generated by Django 4.1.3 on 2022-11-20 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_selling_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('SD', 'Sold'), ('RT', 'Rent'), ('AV', 'Available')], default='AV', max_length=3),
        ),
    ]