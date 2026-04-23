from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Service, Project, ProjectCategory, Testimonial, BlogPost, ContactMessage, AboutPage

def home(request):
    services = Service.objects.all().order_by('order')[:3]
    featured_projects = Project.objects.filter(is_featured=True)[:4]
    testimonials = Testimonial.objects.filter(is_active=True)[:3]
    return render(request, 'core/home.html', {
        'services': services,
        'featured_projects': featured_projects,
        'testimonials': testimonials,
    })

def about(request):
    about_page, _ = AboutPage.objects.get_or_create(id=1)
    return render(request, 'core/about.html', {'about_page': about_page})

def services(request):
    services = Service.objects.all().order_by('order')
    return render(request, 'core/services.html', {'services': services})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'core/service_detail.html', {'service': service})

def portfolio(request):
    categories = ProjectCategory.objects.all()
    projects = Project.objects.all().order_by('-completion_date')
    return render(request, 'core/portfolio.html', {
        'categories': categories,
        'projects': projects,
    })

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'core/project_detail.html', {'project': project})

def testimonials_view(request):
    testimonials = Testimonial.objects.filter(is_active=True)
    return render(request, 'core/testimonials.html', {'testimonials': testimonials})

def blog(request):
    posts = BlogPost.objects.filter(is_published=True).order_by('-publish_date')
    return render(request, 'core/blog.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    return render(request, 'core/blog_detail.html', {'post': post})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        project_type = request.POST.get('project_type')
        budget_range = request.POST.get('budget_range')
        timeline = request.POST.get('timeline')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name, email=email, phone=phone,
            project_type=project_type, budget_range=budget_range,
            timeline=timeline, message=message
        )
        messages.success(request, "Your message has been sent successfully. We will get back to you shortly.")
        return redirect('contact')
        
    return render(request, 'core/contact.html')

def careers(request):
    return render(request, 'core/careers.html')
