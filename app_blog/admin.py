from django.contrib import admin

from .forms import ArticleImageForm
from .models import Article, ArticleImage, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category", "slug")
    search_fields = ("category", "slug")
    prepopulated_fields = {"slug": ("category",)}
    fieldsets = (
        (
            None,
            {
                "fields": ("category", "slug"),
            },
        ),
    )


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 1
    fieldsets = (
        (
            None,
            {
                "fields": ("title", "image"),
            },
        ),
    )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_date", "slug", "main_page")
    list_filter = ("main_page", "pub_date", "category")
    search_fields = ("title", "slug", "description")
    inlines = [ArticleImageInline]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("category",)
    fieldsets = (
        (
            None,
            {
                "fields": ("pub_date", "title", "description", "main_page", "category"),
            },
        ),
        (
            "Додатково",
            {
                "classes": ("collapse",),
                "fields": ("slug",),
            },
        ),
    )

