from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

@register.filter(name='file_type')
def file_type(file_name):
    image = ['jpg', 'jpeg', 'png', 'gif', 'svg']
    document = ['doc', 'docx', 'pdf', 'txt', 'xls', 'xlsx', 'ppt', 'pptx']
    video = ['mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm']
    extension = file_name.split('.')[-1]
    if extension in image:
        return 'image'
    elif extension in document:
        return 'document'
    elif extension in video:
        return 'video'
    else:
        return 'other'