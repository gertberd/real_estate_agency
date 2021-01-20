# Generated by Django 2.2.4 on 2021-01-20 08:58

from django.db import migrations


def fill_owner_from_flat(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    Owner = apps.get_model("property", "Owner")
    for flat in Flat.objects.all():
        owner, _ = Owner.objects.get_or_create(
            name=flat.owner,
            phonenumber=flat.owners_phonenumber,
            pure_phone=flat.owner_pure_phone,
        )
        flat.owners.add(owner)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0011_auto_20210120_1057"),
    ]

    operations = [migrations.RunPython(fill_owner_from_flat)]