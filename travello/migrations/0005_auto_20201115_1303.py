# Generated by Django 3.0.3 on 2020-11-15 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_auto_20201115_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('textarea', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
