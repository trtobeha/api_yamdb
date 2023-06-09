# Generated by Django 3.2 on 2023-05-29 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0001_initial'),
        ('reviews', '0002_auto_20230529_0656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genretitle',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='genretitle',
            name='title',
        ),
        migrations.RemoveField(
            model_name='title',
            name='category',
        ),
        migrations.RemoveField(
            model_name='title',
            name='genre',
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='titles.title'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='GenreTitle',
        ),
        migrations.DeleteModel(
            name='Title',
        ),
    ]
