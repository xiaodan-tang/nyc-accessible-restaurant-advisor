# Generated by Django 3.1.2 on 2020-11-08 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accessible_restaurant', '0006_auto_20201108_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='auth_documents',
            field=models.FileField(null=True, upload_to='documents/pdfs/'),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='auth_status',
            field=models.CharField(choices=[('certified', 'Approve'), ('pending', 'Pending'), ('uncertified', 'Disapprove')], default='pending', max_length=16),
        ),
        migrations.AlterField(
            model_name='approvalpendingusers',
            name='auth_documents',
            field=models.FileField(upload_to='documents/pdfs/'),
        ),
        migrations.AlterField(
            model_name='approvalpendingusers',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auth', to=settings.AUTH_USER_MODEL),
        ),
    ]
