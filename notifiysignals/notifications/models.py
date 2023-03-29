from django.db import models
from django.template.defaultfilters import slugify


class Author(models.Model):
    slug = models.SlugField(
        max_length=255, unique=True, null=False, blank=False, db_index=True
    )
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name.upper()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Author, self).save(*args, **kwargs)


class Book(models.Model):
    slug = models.SlugField(
        max_length=255, unique=True, null=False, blank=False, db_index=True
    )
    title = models.CharField(max_length=255, null=False, blank=True)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    is_published = models.BooleanField(help_text="Is book published.", default=True)
    published_date = models.DateField(auto_created=True)

    def __str__(self):
        return self.title.upper()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Book, self).save(*args, **kwargs)


class Notification(models.Model):
    title = models.CharField(max_length=50, null=False, blank=True)
    description = models.TextField()
    generated_date = models.DateField(auto_now=True, null=True)
    generated_time = models.TimeField(auto_now=True, null=True)

    def save(self, *args, **kwargs):
        return super(Notification, self).save(*args, **kwargs)

    def set_title(self, title: str) -> None:
        self.title = title

    def set_description(self, description: str) -> None:
        self.description = description
