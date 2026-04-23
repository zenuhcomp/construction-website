from django.contrib import admin
from .models import Service, ProjectCategory, Project, ProjectImage, Testimonial, BlogPost, ContactMessage

class RichTextAdminMixin:
    class Media:
        js = (
            'https://cdn.ckeditor.com/4.25.1-lts/standard-all/ckeditor.js',
            'js/admin_ckeditor.js',
        )

@admin.register(Service)
class ServiceAdmin(RichTextAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'order')
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(RichTextAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'completion_date')
    list_filter = ('category', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company', 'is_active')
    list_filter = ('is_active',)

@admin.register(BlogPost)
class BlogPostAdmin(RichTextAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'is_published', 'author')
    list_filter = ('is_published', 'publish_date')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'project_type', 'created_at')
    readonly_fields = ('name', 'email', 'phone', 'project_type', 'budget_range', 'timeline', 'message', 'created_at')
