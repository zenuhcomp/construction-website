from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Service, Project, BlogPost, SiteSettings, AboutPage
from .forms import ServiceForm, ProjectForm, BlogPostForm, SiteSettingsForm, AboutPageForm

class OwnerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = '/login/'
    
    def test_func(self):
        return self.request.user.is_superuser

class DashboardHome(OwnerRequiredMixin, TemplateView):
    template_name = 'core/dashboard/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['service_count'] = Service.objects.count()
        ctx['project_count'] = Project.objects.count()
        ctx['blog_count'] = BlogPost.objects.count()
        return ctx

# --- Services ---
class ServiceList(OwnerRequiredMixin, ListView):
    model = Service
    template_name = 'core/dashboard/list.html'
    context_object_name = 'items'
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['model_name'] = 'Service'
        ctx['add_url'] = 'dashboard_service_add'
        ctx['edit_url'] = 'dashboard_service_edit'
        ctx['delete_url'] = 'dashboard_service_delete'
        return ctx

class ServiceCreate(OwnerRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'core/dashboard/form.html'
    success_url = reverse_lazy('dashboard_services')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Add Service'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, "Service created successfully.")
        return super().form_valid(form)

class ServiceUpdate(OwnerRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'core/dashboard/form.html'
    success_url = reverse_lazy('dashboard_services')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Edit Service'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, "Service updated successfully.")
        return super().form_valid(form)

class ServiceDelete(OwnerRequiredMixin, DeleteView):
    model = Service
    template_name = 'core/dashboard/confirm_delete.html'
    success_url = reverse_lazy('dashboard_services')

# --- Portfolio (Projects) ---
class ProjectList(OwnerRequiredMixin, ListView):
    model = Project
    template_name = 'core/dashboard/list.html'
    context_object_name = 'items'
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['model_name'] = 'Portfolio Project'
        ctx['add_url'] = 'dashboard_project_add'
        ctx['edit_url'] = 'dashboard_project_edit'
        ctx['delete_url'] = 'dashboard_project_delete'
        return ctx

class ProjectCreate(OwnerRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'core/dashboard/form.html'
    success_url = reverse_lazy('dashboard_projects')
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Add Portfolio Project'
        return ctx
        
    def form_valid(self, form):
        messages.success(self.request, "Project created successfully.")
        return super().form_valid(form)

class ProjectUpdate(OwnerRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'core/dashboard/form.html'
    success_url = reverse_lazy('dashboard_projects')
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Edit Portfolio Project'
        return ctx
        
    def form_valid(self, form):
        messages.success(self.request, "Project updated successfully.")
        return super().form_valid(form)

class ProjectDelete(OwnerRequiredMixin, DeleteView):
    model = Project
    template_name = 'core/dashboard/confirm_delete.html'
    success_url = reverse_lazy('dashboard_projects')

# --- Blog ---
class BlogList(OwnerRequiredMixin, ListView):
    model = BlogPost
    template_name = 'core/dashboard/list.html'
    context_object_name = 'items'
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['model_name'] = 'Blog Post'
        ctx['add_url'] = 'dashboard_blog_add'
        ctx['edit_url'] = 'dashboard_blog_edit'
        ctx['delete_url'] = 'dashboard_blog_delete'
        return ctx

class BlogCreate(OwnerRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'core/dashboard/form.html'
    success_url = reverse_lazy('dashboard_blogs')
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Add Blog Post'
        return ctx
        
    def form_valid(self, form):
        messages.success(self.request, "Blog Post created successfully.")
        return super().form_valid(form)

class BlogUpdate(OwnerRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'core/dashboard/form.html'
    success_url = reverse_lazy('dashboard_blogs')
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Edit Blog Post'
        return ctx
        
    def form_valid(self, form):
        messages.success(self.request, "Blog Post updated successfully.")
        return super().form_valid(form)

class BlogDelete(OwnerRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'core/dashboard/confirm_delete.html'
    success_url = reverse_lazy('dashboard_blogs')

# --- Site Settings ---
class SiteSettingsUpdate(OwnerRequiredMixin, UpdateView):
    model = SiteSettings
    form_class = SiteSettingsForm
    template_name = 'core/dashboard/form.html'
    success_url = reverse_lazy('dashboard_home')
    
    def get_object(self):
        obj, created = SiteSettings.objects.get_or_create(id=1)
        return obj

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Global Site Configuration'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, "Global site configuration updated successfully.")
        return super().form_valid(form)

# --- About Page Configuration ---
class AboutPageUpdate(OwnerRequiredMixin, UpdateView):
    model = AboutPage
    form_class = AboutPageForm
    template_name = 'core/dashboard/form.html'
    success_url = reverse_lazy('dashboard_home')
    
    def get_object(self):
        obj, created = AboutPage.objects.get_or_create(id=1)
        return obj

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Manage About Page Content'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, "About page updated successfully.")
        return super().form_valid(form)
