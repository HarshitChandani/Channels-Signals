from django.contrib import admin

from .models import Author, Book, Notification


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    exclude = ["slug"]


class BookAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "author",
        "is_published",
        "published_date",
        "slug",
    ]
    exclude = ["slug"]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Notification)
