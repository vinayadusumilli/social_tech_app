# Generated by Django 5.1.2 on 2024-10-28 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0003_tag_project_featured_image_project_vote_ratio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='vote_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
