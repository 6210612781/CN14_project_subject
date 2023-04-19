# Generated by Django 4.2 on 2023-04-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_student_student_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='post_id',
            field=models.ManyToManyField(blank=True, related_name='postsub', to='database.subject'),
        ),
        migrations.AddField(
            model_name='subject',
            name='pre_id',
            field=models.ManyToManyField(blank=True, related_name='presub', to='database.subject'),
        ),
    ]
