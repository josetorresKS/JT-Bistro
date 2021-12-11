# Generated by Django 3.2.1 on 2021-12-11 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('main-dishes', 'Main-Dishes'), ('kids', 'Kids'), ('hot', 'Hot'), ('burger', 'Burger')], db_index=True, default='others', max_length=14, verbose_name='Category'),
        ),
    ]
