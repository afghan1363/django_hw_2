from django import template

register = template.Library()


@register.filter()
def image_files(file_name):
    if file_name:
        return f'/media/{file_name}'
    return '#'

@register.filter()
def head_image():
    return f'/media/appsss.jpg'
