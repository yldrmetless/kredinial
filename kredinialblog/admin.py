from django.contrib import admin
from .models import BlogPost, Category
from django.contrib.auth.models import User

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author_full_name', 'created_at', 'updated_at', 'get_categories')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'author__username')

    def author_full_name(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"
    author_full_name.short_description = 'Author'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['queryset'] = User.objects.filter(pk=request.user.pk)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories.short_description = 'Categories'
