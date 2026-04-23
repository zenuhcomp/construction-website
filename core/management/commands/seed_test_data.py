from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from core.models import Service, ProjectCategory, Project, BlogPost, SiteSettings, AboutPage
import os
import shutil

class Command(BaseCommand):
    help = 'Seeds the database with test construction data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Clearing old data...")
        Service.objects.all().delete()
        ProjectCategory.objects.all().delete()
        Project.objects.all().delete()
        BlogPost.objects.all().delete()
        SiteSettings.objects.all().delete()
        AboutPage.objects.all().delete()
        
        self.stdout.write("Initializing Site Settings...")
        SiteSettings.objects.create(
            company_name="Apex Construction",
            hero_title="Building Excellence, Engineering the Future.",
            hero_subtitle="Premium Commercial & Residential Construction Delivered with Precision",
            contact_email="sales@apexconstruct.com"
        )

        self.stdout.write("Initializing About Page...")
        AboutPage.objects.create(
            hero_title="About Apex Construction",
            hero_subtitle="Mastering the Art of Construction Since 1995",
            image="about/about_us_image.png",
            content_title="Our Heritage & Legacy",
            content_intro="We are more than just builders; we are strategic partners in bringing your vision to life.",
            content_body="<p>Since our founding, we have been committed to delivering projects of the highest quality, safely, on time, and within budget. Our expertise spans residential luxury homes to massive commercial structures.</p><p>We employ cutting-edge technology and proven management systems, ensuring seamless coordination from ground-breaking to handover.</p>"
        )

        self.stdout.write("Populating Services...")
        services_data = [
            {
                "title": "New Home Builds",
                "short_description": "Turnkey solutions for your custom dream home, built from the ground up to exacting standards.",
                "full_description": "We specialize in the full lifecycle of custom residential construction...",
                "icon_image": "services/icons/home_icon.png",
                "cover_image": "services/home_cover.png",
                "order": 1
            },
            {
                "title": "Commercial Construction",
                "short_description": "High-performance commercial spaces designed to drive your business forward.",
                "full_description": "Our commercial construction team delivers high-quality offices...",
                "icon_image": "services/icons/commercial_icon.png",
                "cover_image": "services/commercial_cover.png",
                "order": 2
            },
            {
                "title": "Renovations & Extensions",
                "short_description": "Transforming existing properties into modern spaces of elegance.",
                "full_description": "Whether it is a historic restoration or a modern structural extension...",
                "icon_image": "services/icons/renovation_icon.png",
                "cover_image": "services/renovation_cover.png",
                "order": 3
            },
            {
                "title": "Project Management",
                "short_description": "Expert oversight navigating budgeting, procurement, and site coordination.",
                "full_description": "We offer independent project management services for large-scale developments...",
                "icon_image": "services/icons/management_icon.png",
                "cover_image": "services/management_cover.png",
                "order": 4
            }
        ]
        for s in services_data:
            Service.objects.create(**s)

        self.stdout.write("Populating Project Categories...")
        cats = ['Residential', 'Commercial', 'Industrial', 'Restoration']
        cat_objs = {}
        for c in cats:
            cat_objs[c] = ProjectCategory.objects.create(name=c)

        self.stdout.write("Populating Portfolio Projects...")
        projects_data = [
            {
                "title": "The Azure Coast Villa",
                "category": cat_objs["Residential"],
                "client": "Private Estate Group",
                "scope": "Full build, interior finishing, landscaping.",
                "duration": "14 Months",
                "completion_date": "2025-11-15",
                "cover_image": "projects/modern_villa_1776515266218.png",
                "description": "A stunning 10,000 sq.ft modern luxury villa featuring sweeping ocean views, an infinity pool, and integrated smart-home technology. We utilized post-tensioned concrete for expansive column-free living areas.",
                "testimonial_quote": "The team exceeded our expectations, delivering a true architectural masterpiece.",
                "is_featured": True
            },
            {
                "title": "TechHub Innovation Center",
                "category": cat_objs["Commercial"],
                "client": "TechCorp Ventures",
                "scope": "Core and shell, full tenant improvements.",
                "duration": "22 Months",
                "completion_date": "2024-08-10",
                "cover_image": "projects/commercial_tower_1776515315100.png",
                "description": "A cutting-edge commercial tower spanning 15 floors. The project features a LEED Platinum certified HVAC system, curtain wall glass exteriors, and a fully landscaped rooftop terrace.",
                "testimonial_quote": "Their commitment to safety and schedule was vital to our corporate transition.",
                "is_featured": True
            },
            {
                "title": "Heritage Downtown Restoration",
                "category": cat_objs["Restoration"],
                "client": "City Historical Society",
                "scope": "Structural stabilization, facade restoration.",
                "duration": "9 Months",
                "completion_date": "2023-05-20",
                "cover_image": "projects/historic_building_restoration_1776515345563.png",
                "description": "We carefully rejuvenated a 19th-century municipal building, updating life-safety systems while flawlessly preserving the intricate masonry and original woodwork.",
                "testimonial_quote": "They respected the history while preparing the building for the next century.",
                "is_featured": False
            },
            {
                "title": "Summit Logistics Park",
                "category": cat_objs["Industrial"],
                "client": "Global Freight Solutions",
                "scope": "Warehouse construction, heavy-duty paving.",
                "duration": "18 Months",
                "completion_date": "2025-01-30",
                "cover_image": "projects/industrial_warehouse_1776515374084.png",
                "description": "A massive 500,000 sq.ft industrial park equipped with advanced loading bays, cross-docking facilities, and reinforced concrete flooring to support heavy industrial loads.",
                "testimonial_quote": "Delivered on time and within the incredibly tight budget constraints.",
                "is_featured": True
            },
            {
                "title": "Modernist Desert Retreat",
                "category": cat_objs["Residential"],
                "client": "Smith Family",
                "scope": "Custom home build, off-grid systems.",
                "duration": "11 Months",
                "completion_date": "2024-12-05",
                "cover_image": "projects/desert_home_1776515412765.png",
                "description": "An off-grid eco-friendly residence blending seamlessly into the desert landscape. Using rammed earth walls and massive solar arrays, the home acts as its own self-sustaining utility.",
                "testimonial_quote": "A perfectly executed build facing intense environmental challenges.",
                "is_featured": False
            },
            {
                "title": "Horizon Retail Plaza",
                "category": cat_objs["Commercial"],
                "client": "Horizon Equities",
                "scope": "General contracting, site development.",
                "duration": "16 Months",
                "completion_date": "2026-03-01",
                "cover_image": "projects/retail_plaza_1776515447003.png",
                "description": "A dynamic multi-tenant retail plaza incorporating vast open-air walkways, subterranean parking, and high-end restaurant build-outs.",
                "testimonial_quote": "The build quality has attracted premium brands to our plaza instantly.",
                "is_featured": True
            }
        ]
        
        for p in projects_data:
            Project.objects.create(**p)

        self.stdout.write("Populating Blog Posts...")
        now = timezone.now()
        blogs_data = [
            {
                "title": "The Future of Sustainable Concrete",
                "author": "Engineering",
                "image": "blog/blog_concrete.png",
                "content": "<p>Concrete is the backbone of modern construction...</p>",
                "publish_date": now - timedelta(days=2),
                "is_published": True
            },
            {
                "title": "Navigating Supply Chain Volatility",
                "author": "Procurement",
                "image": "blog/blog_supply_chain.png",
                "content": "<p>Global supply chain disruptions continue to pose a threat...</p>",
                "publish_date": now - timedelta(days=15),
                "is_published": True
            }
        ]
        for b in blogs_data:
            BlogPost.objects.create(**b)

        self.stdout.write(self.style.SUCCESS('Successfully seeded development database!'))
