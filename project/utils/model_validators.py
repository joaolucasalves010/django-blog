from django.core.exceptions import ValidationError

def validate_image(image):
  if not image.name.lower().endswith('.png'):
    raise ValidationError("A imagem precisa está no formato de PNG")