import os
import django
from django.utils import timezone
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Service, ProjectCategory, Project, BlogPost

def populate():
    print("Clearing old data...")
    Service.objects.all().delete()
    ProjectCategory.objects.all().delete()
    Project.objects.all().delete()
    BlogPost.objects.all().delete()

    print("Populating Services...")
    services_data = [
        {
            "title": "New Home Builds",
            "icon": "fas fa-home",
            "short_description": "Turnkey solutions for your custom dream home, built from the ground up to exacting standards.",
            "full_description": "We specialize in the full lifecycle of custom residential construction. From initial architectural planning and permitting to the final landscaping and handover. Our dedicated project managers ensure that every aspect of your new home is built with precision, utilizing sustainable materials and state-of-the-art engineering.",
            "order": 1
        },
        {
            "title": "Commercial Construction",
            "icon": "fas fa-city",
            "short_description": "High-performance commercial spaces designed to drive your business forward.",
            "full_description": "Our commercial construction team delivers high-quality offices, retail spaces, and mixed-use developments. We understand the critical nature of minimizing downtime and meeting strict completion schedules, ensuring your business operations can scale without delay.",
            "order": 2
        },
        {
            "title": "Renovations & Extensions",
            "icon": "fas fa-tools",
            "short_description": "Transforming existing properties into modern spaces of elegance and updated functionality.",
            "full_description": "Whether it is a historic restoration or a modern structural extension, our renovation experts meticulously blend new construction with the original architecture. We handle complex zoning laws and structural upgrades, providing a seamless transformation.",
            "order": 3
        },
        {
            "title": "Project Management",
            "icon": "fas fa-tasks",
            "short_description": "Expert oversight navigating budgeting, procurement, and site coordination.",
            "full_description": "We offer independent project management services for large-scale developments. Our proactive approach ensures risks are mitigated, budgets are strictly managed, and subcontractors operate at peak efficiency from inception to close-out.",
            "order": 4
        }
    ]
    for s in services_data:
        Service.objects.create(**s)

    print("Populating Project Categories...")
    cats = ['Residential', 'Commercial', 'Industrial', 'Restoration']
    cat_objs = {}
    for c in cats:
        cat_objs[c] = ProjectCategory.objects.create(name=c)

    print("Populating Portfolio Projects...")
    projects_data = [
        {
            "title": "The Azure Coast Villa",
            "category": cat_objs["Residential"],
            "client": "Private Estate Group",
            "scope": "Full build, interior finishing, landscaping.",
            "duration": "14 Months",
            "completion_date": "2025-11-15",
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
            "description": "A dynamic multi-tenant retail plaza incorporating vast open-air walkways, subterranean parking, and high-end restaurant build-outs.",
            "testimonial_quote": "The build quality has attracted premium brands to our plaza instantly.",
            "is_featured": True
        }
    ]
    for p in projects_data:
        Project.objects.create(**p)

    print("Populating Blog Posts...")
    now = timezone.now()
    blogs_data = [
        {
            "title": "The Future of Sustainable Concrete: Greener Building Practices",
            "author": "Marcus Thorne, Head Engineer",
            "content": "<p>Concrete is the backbone of modern construction, yet its carbon footprint is undeniable. In this article, we explore the rise of <strong>geopolymer concrete</strong> and supplementary cementitious materials (SCMs) such as fly ash and slag.</p><p>By reducing the reliance on traditional Portland cement, the industry has discovered methods to cut emissions by up to 80% without sacrificing structural integrity.</p><h3>Why it Matters</h3><p>For large-scale commercial developers, utilizing sustainable concrete not only earns critical LEED certification points but also future-proofs the asset against impending carbon-tax regulations.</p>",
            "publish_date": now - timedelta(days=2),
            "is_published": True
        },
        {
            "title": "Navigating Supply Chain Volatility in 2026",
            "author": "Sarah Jenkins, Procurement Director",
            "content": "<p>Global supply chain disruptions continue to pose a threat to project timelines. From structural steel to specialty glass, lead times have fluctuated wildly over the past year.</p><p>We have adapted by executing <em>early procurement strategies</em> and leveraging local manufacturing where possible. In our latest project, the TechHub Innovation Center, bulk ordering materials during the schematic design phase saved the client over $1.2M in escalation costs.</p><p>Keys to mitigating risk include locking in unit prices early, establishing multiple vendor contingencies, and utilizing pre-fabrication.</p>",
            "publish_date": now - timedelta(days=15),
            "is_published": True
        },
        {
            "title": "5 Emerging Trends in Luxury Home Architecture",
            "author": "Elena Rossi, Lead Architect",
            "content": "<p>Luxury clients are moving away from bloated mega-mansions and focusing intensely on wellbeing, integration with nature, and cutting-edge unseen technology. Here are the top 5 trends we are building today:</p><ul><li><strong>Biophilic Design:</strong> Bringing the outside in through massive operable glass walls and indoor gardens.</li><li><strong>Wellness Centers:</strong> Dedicated spa areas featuring cold plunges, infrared saunas, and salt rooms.</li><li><strong>Invisible Smart Home Tech:</strong> Speakers built directly within drywall and climate systems governed by AI.</li><li><strong>Energy Autonomy:</strong> Fully integrated solar roof tiles paired with commercial-grade battery banks.</li><li><strong>Acoustic Isolation:</strong> Sound-engineered recording/theater rooms completely decoupled from the main framing.</li></ul>",
            "publish_date": now - timedelta(days=32),
            "is_published": True
        },
        {
            "title": "Restoring History: The Unique Challenges of Heritage Projects",
            "author": "James Croft, Restoration Manager",
            "content": "<p>Working on a building that is over 100 years old is an exercise in surgical precision. Unlike new builds where the environment is perfectly controlled, restoration is full of surprises.</p><p>During the Heritage Downtown Restoration project, our engineering team discovered foundation settling that standard radar failed to detect. The solution required injecting high-density geopolymer resins under the footings, permanently stabilizing the structure without the need for invasive excavation.</p><p>At the end of the day, our goal is to render our work invisible—preserving the history while secretly fortifying the structure for modern use.</p>",
            "publish_date": now - timedelta(days=45),
            "is_published": True
        },
        {
            "title": "Safety First, Always: Our Zero-Incident Strategy",
            "author": "David Vance, HSE Director",
            "content": "<p>At Premium Builders, a 100% safety record isn't just a marketing slogan; it's a daily, relentless commitment. Construction remains one of the highest-risk industries globally, but injuries are preventable.</p><p>We recently implemented ultra-wideband (UWB) proximity sensors on all heavy machinery across our active sites. If a worker steps into a blind spot, the machine automatically throttles down, and the operator is instantly alerted.</p><p>Combined with daily mandatory morning briefings (toolbox talks) and rigorous behavioral safety training, we maintain an environment where everyone goes home safely.</p>",
            "publish_date": now - timedelta(days=60),
            "is_published": True
        }
    ]
    for b in blogs_data:
        BlogPost.objects.create(**b)

    print("Database populated successfully!")

if __name__ == '__main__':
    populate()
