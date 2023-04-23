# Generated by Django 4.1.7 on 2023-03-31 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=30)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=30)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.FloatField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='username', max_length=30)),
                ('fname', models.CharField(default='None', max_length=30, null=True)),
                ('lname', models.CharField(default='None', max_length=30, null=True)),
                ('age', models.IntegerField(default='None', null=True)),
                ('password', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=30)),
                ('stock', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='images/')),
                ('is_active', models.BooleanField(default=True)),
                ('categoryName', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='categoryName', to='market.category')),
                ('orderNumber', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_orders', to='market.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(blank=True, related_name='order_items', to='market.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='market.user'),
        ),
    ]