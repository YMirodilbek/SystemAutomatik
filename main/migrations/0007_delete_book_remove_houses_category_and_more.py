# Generated by Django 5.2.1 on 2025-05-25 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_qulayliklar_remove_students_classes_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.RemoveField(
            model_name='houses',
            name='category',
        ),
        migrations.RemoveField(
            model_name='houses',
            name='qulayliklar',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
        migrations.DeleteModel(
            name='Youtube',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Houses',
        ),
        migrations.DeleteModel(
            name='Qulayliklar',
        ),
    ]
