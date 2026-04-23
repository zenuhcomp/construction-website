import os
import shutil
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Project

source_dir = "/home/kibsoft/.gemini/antigravity/brain/0912e103-a9cc-4379-a00b-4896e8403051"
dest_dir = "/home/kibsoft/Documents/projects/construction/website/media/projects"
os.makedirs(dest_dir, exist_ok=True)

# Find generated images
images = os.listdir(source_dir)

mapping = {
    "The Azure Coast Villa": "modern_villa",
    "TechHub Innovation Center": "commercial_tower",
    "Heritage Downtown Restoration": "historic_building_restoration",
    "Summit Logistics Park": "industrial_warehouse",
    "Modernist Desert Retreat": "desert_home",
    "Horizon Retail Plaza": "retail_plaza"
}

for title, img_prefix in mapping.items():
    # Find exact matching filename
    matching_files = [f for f in images if f.startswith(img_prefix) and f.endswith('.png')]
    if matching_files:
        src_path = os.path.join(source_dir, matching_files[0])
        safe_filename = matching_files[0]
        dst_path = os.path.join(dest_dir, safe_filename)
        
        # Copy file
        shutil.copy2(src_path, dst_path)
        
        # Update Project
        try:
            p = Project.objects.get(title=title)
            # Django expects relative path from MEDIA_ROOT for ImageField
            p.cover_image = f"projects/{safe_filename}"
            p.save()
            print(f"Updated {title} with {safe_filename}")
        except Project.DoesNotExist:
            print(f"Could not find project {title}")
