from django.db import models
from django.utils.text import slugify


class AutoSlugMixin(models.Model):
    """Миксин для генерации слага на основе имени модели."""

    slug_field_name = "slug"
    slug_source_field_name = "name"

    class Meta:
        abstract = True

    def generate_unique_slug(self):
        source = getattr(self, self.slug_source_field_name)
        base_slug = slugify(source)
        slug = base_slug
        counter = 1

        while (
            self.__class__.objects.filter(**{self.slug_field_name: slug})
            .exclude(pk=self.pk)
            .exists()
        ):
            slug = f"{base_slug}-{counter}"
            counter += 1

        return slug

    def save(self, *args, **kwargs):
        if not getattr(self, self.slug_field_name):
            slug = self.generate_unique_slug()
            setattr(self, self.slug_field_name, slug)
        super().save(*args, **kwargs)
