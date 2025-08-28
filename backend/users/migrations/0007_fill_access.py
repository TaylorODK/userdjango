from django.db import migrations


def create_access(apps, schema_editor):
    Access = apps.get_model("users", "AccessRolesRule")
    Role = apps.get_model("users", "Role")
    Element = apps.get_model("users", "BusinessElement")

    for role in Role.objects.all():
        for element in Element.objects.all():
            role = role
            element = element
            if role.slug == "admin" or role.slug == "manager":
                Access.objects.get_or_create(
                    role=role,
                    element=element,
                    read_permission=True,
                    read_all_permission=True,
                    create_permission=True,
                    update_permission=True,
                    update_all_permission=True,
                    delete_permission=True,
                    delete_all_permission=True,
                )
            elif role.slug == "user" and element.slug == "product":
                Access.objects.get_or_create(
                    role=role,
                    element=element,
                    read_permission=True,
                    read_all_permission=True,
                    create_permission=False,
                    update_permission=False,
                    update_all_permission=False,
                    delete_permission=False,
                    delete_all_permission=False,
                )
            elif role.slug == "user" and element.slug == "order":
                Access.objects.get_or_create(
                    role=role,
                    element=element,
                    read_permission=True,
                    read_all_permission=False,
                    create_permission=True,
                    update_permission=True,
                    update_all_permission=False,
                    delete_permission=True,
                    delete_all_permission=False,
                )
            elif role.slug == "guest" and element.slug == "product":
                Access.objects.get_or_create(
                    role=role,
                    element=element,
                    read_permission=True,
                    read_all_permission=True,
                    create_permission=False,
                    update_permission=False,
                    update_all_permission=False,
                    delete_permission=False,
                    delete_all_permission=False,
                )
            else:
                Access.objects.get_or_create(
                    role=role,
                    element=element,
                    read_permission=False,
                    read_all_permission=False,
                    create_permission=False,
                    update_permission=False,
                    update_all_permission=False,
                    delete_permission=False,
                    delete_all_permission=False,
                )




class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_createsuperuser"),
    ]

    operations = [
        migrations.RunPython(create_access),
    ]
