from django import forms
from .models import Service, Project, BlogPost, SiteSettings, AboutPage

class CustomModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.NumberInput, forms.Select, forms.URLInput)):
                field.widget.attrs['class'] = 'form-control mb-3'
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input mb-3'
            elif isinstance(field.widget, forms.FileInput):
                field.widget.attrs['class'] = 'form-control mb-3'
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = 'form-control mb-3 ckeditor-textarea'
                
class ServiceForm(CustomModelForm):
    class Meta:
        model = Service
        fields = ['title', 'icon_image', 'cover_image', 'short_description', 'full_description', 'order']

class ProjectForm(CustomModelForm):
    class Meta:
        model = Project
        fields = ['title', 'category', 'client', 'scope', 'duration', 'completion_date', 'cover_image', 'description', 'testimonial_quote', 'is_featured']
        widgets = {
            'completion_date': forms.DateInput(attrs={'type': 'date'}),
        }

class BlogPostForm(CustomModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'image', 'content', 'publish_date', 'is_published']
        widgets = {
            'publish_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class SiteSettingsForm(CustomModelForm):
    class Meta:
        model = SiteSettings
        fields = '__all__'

class AboutPageForm(CustomModelForm):
    class Meta:
        model = AboutPage
        fields = '__all__'
