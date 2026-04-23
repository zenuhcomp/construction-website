from django.db import models
from django.utils.text import slugify
from .utils import process_and_convert_image

class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    icon_image = models.ImageField(upload_to="services/icons/", blank=True, null=True, help_text="Upload an icon image")
    cover_image = models.ImageField(upload_to="services/", blank=True, null=True)
    short_description = models.TextField()
    full_description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        process_and_convert_image(self.icon_image, max_size=(256, 256))
        process_and_convert_image(self.cover_image, max_size=(1200, 1200))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = 'Project Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True, related_name='projects')
    client = models.CharField(max_length=200, blank=True)
    scope = models.CharField(max_length=300, blank=True)
    duration = models.CharField(max_length=100, blank=True)
    completion_date = models.DateField(null=True, blank=True)
    cover_image = models.ImageField(upload_to="projects/")
    description = models.TextField()
    testimonial_quote = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        process_and_convert_image(self.cover_image, max_size=(1200, 1200))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to="projects/gallery/")
    caption = models.CharField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        process_and_convert_image(self.image, max_size=(1200, 1200))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.project.title} Image"

class Testimonial(models.Model):
    client_name = models.CharField(max_length=150)
    client_role = models.CharField(max_length=150, blank=True)
    company = models.CharField(max_length=150, blank=True)
    logo = models.ImageField(upload_to="testimonials/logos/", blank=True, null=True)
    text = models.TextField()
    video_url = models.URLField(blank=True, help_text="YouTube/Vimeo embed URL")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        process_and_convert_image(self.logo, max_size=(400, 400))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Testimonial from {self.client_name}"

class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=100, default='Admin')
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    content = models.TextField()
    publish_date = models.DateTimeField()
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        process_and_convert_image(self.image, max_size=(1200, 1200))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    project_type = models.CharField(max_length=100, blank=True)
    budget_range = models.CharField(max_length=100, blank=True)
    timeline = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"

class SiteSettings(models.Model):
    company_name = models.CharField(max_length=150, default="Premium Builders")
    hero_title = models.CharField(max_length=200, default="Building Excellence, Engineering the Future.")
    hero_subtitle = models.CharField(max_length=300, default="Premium Commercial & Residential Construction Delivered with Precision")
    about_snippet = models.TextField(default="Reliability, precision, and excellence in every project. Building the future sustainably and professionally.")
    about_page_text = models.TextField(default="Since our founding, we have been committed to delivering projects of the highest quality...")
    contact_phone = models.CharField(max_length=50, default="+1 (234) 567-890")
    contact_email = models.EmailField(default="info@premiumbuilders.com")
    contact_address = models.CharField(max_length=300, default="123 Construction Blvd, City")
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    # Hero Buttons
    hero_cta_primary = models.CharField(max_length=50, default="Request a Free Quote")
    hero_cta_secondary = models.CharField(max_length=50, default="View Our Work")

    # Stats Section
    stat_1_value = models.CharField(max_length=50, default="20+ Years")
    stat_1_label = models.CharField(max_length=50, default="Experience")
    stat_2_value = models.CharField(max_length=50, default="ISO 9001")
    stat_2_label = models.CharField(max_length=50, default="Generated")
    stat_3_value = models.CharField(max_length=50, default="500+")
    stat_3_label = models.CharField(max_length=50, default="Projects Completed")
    stat_4_value = models.CharField(max_length=50, default="100%")
    stat_4_label = models.CharField(max_length=50, default="Safety Record")

    def __str__(self):
        return "Global Site Settings"

class AboutPage(models.Model):
    hero_title = models.CharField(max_length=200, default="About Our Company")
    hero_subtitle = models.CharField(max_length=300, default="Mastering the Art of Construction Since 2005")
    image = models.ImageField(upload_to="about/", blank=True, null=True)
    content_title = models.CharField(max_length=200, default="Our Heritage")
    content_intro = models.TextField(default="We are more than just builders; we are partners in bringing your vision to life.")
    content_body = models.TextField(default="Since our founding...\n\nWe employ cutting-edge technology...")
    
    def save(self, *args, **kwargs):
        process_and_convert_image(self.image, max_size=(1000, 1000))
        super().save(*args, **kwargs)
        
    def __str__(self):
        return "About Page Content"
