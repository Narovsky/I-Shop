# Generated by Django 2.2 on 2019-04-30 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='catalog.Item')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='cart.Cart')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='catalog.Item')),
            ],
        ),
    ]
