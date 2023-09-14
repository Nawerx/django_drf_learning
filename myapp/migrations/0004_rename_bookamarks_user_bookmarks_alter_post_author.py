# Generated by Django 4.2.4 on 2023-09-14 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user_bookamarks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='bookamarks',
            new_name='bookmarks',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(db_column='author_id', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
