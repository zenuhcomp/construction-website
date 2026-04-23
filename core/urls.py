from django.urls import path
from django.contrib.auth import views as auth_views
from . import views, dashboard_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/<slug:slug>/', views.project_detail, name='project_detail'),
    path('testimonials/', views.testimonials_view, name='testimonials'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('careers/', views.careers, name='careers'),
    
    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    
    # Dashboard
    path('content/', dashboard_views.DashboardHome.as_view(), name='dashboard_home'),
    path('content/settings/', dashboard_views.SiteSettingsUpdate.as_view(), name='dashboard_settings'),
    path('content/about/', dashboard_views.AboutPageUpdate.as_view(), name='dashboard_about'),
    
    path('content/services/', dashboard_views.ServiceList.as_view(), name='dashboard_services'),
    path('content/services/add/', dashboard_views.ServiceCreate.as_view(), name='dashboard_service_add'),
    path('content/services/<int:pk>/edit/', dashboard_views.ServiceUpdate.as_view(), name='dashboard_service_edit'),
    path('content/services/<int:pk>/delete/', dashboard_views.ServiceDelete.as_view(), name='dashboard_service_delete'),
    
    path('content/portfolio/', dashboard_views.ProjectList.as_view(), name='dashboard_projects'),
    path('content/portfolio/add/', dashboard_views.ProjectCreate.as_view(), name='dashboard_project_add'),
    path('content/portfolio/<int:pk>/edit/', dashboard_views.ProjectUpdate.as_view(), name='dashboard_project_edit'),
    path('content/portfolio/<int:pk>/delete/', dashboard_views.ProjectDelete.as_view(), name='dashboard_project_delete'),
    
    path('content/blog/', dashboard_views.BlogList.as_view(), name='dashboard_blogs'),
    path('content/blog/add/', dashboard_views.BlogCreate.as_view(), name='dashboard_blog_add'),
    path('content/blog/<int:pk>/edit/', dashboard_views.BlogUpdate.as_view(), name='dashboard_blog_edit'),
    path('content/blog/<int:pk>/delete/', dashboard_views.BlogDelete.as_view(), name='dashboard_blog_delete'),
]
