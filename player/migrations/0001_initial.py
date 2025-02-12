# Generated by Django 5.1 on 2024-11-29 15:54

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('developers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='players',
            fields=[
                ('Players_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('username', models.CharField(max_length=6, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='Password')),
                ('contact', models.CharField(max_length=10, verbose_name='Contact')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=10, verbose_name='Status')),
                ('profile_image', models.ImageField(blank=True, default='C:\\Users\\asus\\Documents\\steam\\player\\static\\player\\images\\profileimages\\profile-user.png', null=True, upload_to='profile_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100, unique=True)),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_status', models.CharField(default='Pending', max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='developers.game')),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchased_on', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='developers.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.players')),
            ],
        ),
    ]
