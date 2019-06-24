# Generated by Django 2.0 on 2019-06-24 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=11)),
                ('school', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extension', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
