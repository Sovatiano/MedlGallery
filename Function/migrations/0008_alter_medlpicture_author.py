# Generated by Django 4.0.4 on 2022-04-21 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Function', '0007_alter_medlpicture_author_alter_medltag_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medlpicture',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
