from django.db import migrations
from django.utils.text import slugify


def create_business_elements(apps, schema_editor):
    """
    Автоматическое заполнение таблицы BusinessElement
    на основе созданных моделей.
    """
    BusinessElement = apps.get_model("users", "BusinessElement")

    for model in apps.get_app_config("api").get_models():
        model_name = model._meta.verbose_name.title()
        model_slug = model._meta.model_name

        BusinessElement.objects.get_or_create(
            name=model_name,
            slug=slugify(model_slug),
            defaults={"description": f"Доступ к модели {model_name}"},
        )


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_business_elements),
    ]
