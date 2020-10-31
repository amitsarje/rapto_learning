# Generated by Django 3.0.8 on 2020-10-21 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='name',
            new_name='Title',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='prize',
        ),
        migrations.AddField(
            model_name='courses',
            name='Description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='Image',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='Objective',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='Requirements',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='Subtitle',
            field=models.CharField(max_length=150, null=True),
        ),
    ]