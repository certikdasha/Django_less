# Generated by Django 3.1.7 on 2021-03-04 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20210302_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_to_comm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.comment'),
        ),
    ]
