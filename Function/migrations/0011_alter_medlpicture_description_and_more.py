# Generated by Django 4.0.4 on 2022-04-22 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Function', '0010_alter_medltag_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medlpicture',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='medltag',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
