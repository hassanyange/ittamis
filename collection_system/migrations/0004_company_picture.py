# Generated by Django 4.2.10 on 2024-03-02 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_system', '0003_company_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
