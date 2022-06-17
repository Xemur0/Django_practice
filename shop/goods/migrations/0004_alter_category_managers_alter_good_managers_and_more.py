# Generated by Django 4.0.4 on 2022-06-01 14:24

import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('goods', '0003_good_site'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
                ('current_site', django.contrib.sites.managers.CurrentSiteManager('site')),
            ],
        ),
        migrations.AlterModelManagers(
            name='good',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('current_site', django.contrib.sites.managers.CurrentSiteManager('site')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
        ),
    ]
