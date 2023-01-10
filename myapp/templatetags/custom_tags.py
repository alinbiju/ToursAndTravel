from django import template

register = template.Library()

@register.simple_tag()
def getHalfContent(pack_details):
    return pack_details[:int(len(pack_details/5))]
