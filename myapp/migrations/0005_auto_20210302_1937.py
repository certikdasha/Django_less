# Generated by Django 3.1.7 on 2021-03-02 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210302_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklibrary',
            name='book_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.bookuser'),
        ),
    ]
