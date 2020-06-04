# Generated by Django 2.2.10 on 2020-05-29 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Catégorie de menu',
                'verbose_name_plural': 'Catégories de menu',
            },
        ),
    ]