# Generated by Django 2.0.6 on 2018-06-25 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=255)),
                ('is_bought', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='items_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppinglist.ItemsList', verbose_name='List of items'),
        ),
    ]
