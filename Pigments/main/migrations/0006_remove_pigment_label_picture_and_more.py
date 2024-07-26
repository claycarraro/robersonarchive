# Generated by Django 4.2.14 on 2024-07-17 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_material_archive_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pigment',
            name='label_picture',
        ),
        migrations.AlterField(
            model_name='material',
            name='archive_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='factory',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='geographical_origins',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='m_pictures',
            field=models.ImageField(blank=True, null=True, upload_to='static/IMGM/'),
        ),
        migrations.AlterField(
            model_name='pigment',
            name='archive_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pigment',
            name='bottle_picture',
            field=models.ImageField(upload_to='IMGB/'),
        ),
        migrations.AlterField(
            model_name='pigment',
            name='chemical_composition',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pigment',
            name='date_of_production',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pigment',
            name='geographical_origins',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pigment',
            name='specific_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
