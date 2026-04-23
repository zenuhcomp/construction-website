import os
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile

def process_and_convert_image(image_field, max_size=None):
    """
    Converts an uploaded image to WEBP and resizes it if needed.
    Only processes if the file is not already a .webp.
    """
    if not image_field:
        return

    # If it's already converted, skip
    if image_field.name.lower().endswith('.webp'):
        return
        
    try:
        # We must read from the file
        image_field.file.seek(0)
        img = Image.open(image_field.file)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    # Convert to RGB (to ensure compatibility with WEBP)
    if img.mode in ("RGBA", "P"):
        # For RGBA, we could keep alpha if WEBP supports it, but simple RGB conversion is safer.
        # Actually WEBP supports alpha. But if we convert to RGB it flattens it.
        # Let's preserve alpha for icons, WEBP handles RGBA perfectly.
        pass
        
    if max_size:
        # Resize maintaining aspect ratio
        img.thumbnail(max_size, Image.Resampling.LANCZOS)

    output = BytesIO()
    # Save as WEBP
    img.save(output, format='WEBP', quality=85)
    output.seek(0)

    # Replace the file content and change extension to .webp
    new_name = os.path.splitext(os.path.basename(image_field.name))[0] + '.webp'
    image_field.save(new_name, ContentFile(output.read()), save=False)
