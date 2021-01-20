# Generated by Django 2.2.4 on 2021-01-19 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0004_auto_20210119_0022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='claims', to=settings.AUTH_USER_MODEL)),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to='property.Flat')),
            ],
        ),
    ]