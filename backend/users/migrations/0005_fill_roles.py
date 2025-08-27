from django.db import migrations, models
from django.utils.text import slugify
from effictivemobile.constants import USERS_ROLE


def create_roles(apps, schema_editor):
    Role = apps.get_model("users", "Role")

    for role_name, role_slug in USERS_ROLE.items():
        model_name = role_name
        model_slug = role_slug

        Role.objects.get_or_create(
            name=model_name,
            slug=model_slug.lower(),
            defaults={"description": f"Роль {model_name}"}
        )


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_usermodel_username_usermodel_unique_user"),
    ]
    operations = [
        migrations.RunPython(create_roles),
    ]
