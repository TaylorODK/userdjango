from django.db import migrations
from django.utils.text import slugify
from effictivemobile.constants import USERS_ROLE
from django.contrib.auth.hashers import make_password


def create_superuser(apps, schema_editor):
    User = apps.get_model("users", "UserModel")
    User.objects.get_or_create(
        first_name="First_name",
        last_name="Last_name",
        email="admn@mail.ru",
        username="admin",
        password=make_password("123456"),
        is_staff=True,
        is_superuser=True,
        role_id=1
    )


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_fill_roles"),
    ]
    operations = [
        migrations.RunPython(create_superuser),
    ]
